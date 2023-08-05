// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at https://mozilla.org/MPL/2.0/.

use inherent::inherent;
use std::{collections::HashMap, marker::PhantomData, sync::Arc};

use glean_core::metrics::MetricType;
use glean_core::traits;

use crate::{ErrorType, RecordedEvent};

pub use glean_core::traits::NoExtraKeys;

// We need to wrap the glean-core type: otherwise if we try to implement
// the trait for the metric in `glean_core::metrics` we hit error[E0117]:
// only traits defined in the current crate can be implemented for arbitrary
// types.

/// Developer-facing API for recording event metrics.
///
/// Instances of this class type are automatically generated by the parsers
/// at build time, allowing developers to record values that were previously
/// registered in the metrics.yaml file.
#[derive(Clone)]
pub struct EventMetric<K> {
    pub(crate) inner: Arc<glean_core::metrics::EventMetric>,
    extra_keys: PhantomData<K>,
}

impl<K: traits::ExtraKeys> EventMetric<K> {
    /// The public constructor used by automatically generated metrics.
    pub fn new(meta: glean_core::CommonMetricData) -> Self {
        let allowed_extra_keys = K::ALLOWED_KEYS.iter().map(|s| s.to_string()).collect();
        let inner = Arc::new(glean_core::metrics::EventMetric::new(
            meta,
            allowed_extra_keys,
        ));
        Self {
            inner,
            extra_keys: PhantomData,
        }
    }

    /// Record a new event with a provided timestamp.
    ///
    /// It's the caller's responsibility to ensure the timestamp comes from the same clock source.
    /// Use [`glean::get_timestamp_ms`](crate::get_timestamp_ms) to get a valid timestamp.
    pub fn record_with_time(&self, timestamp: u64, extra: HashMap<i32, String>) {
        let metric = Arc::clone(&self.inner);
        crate::launch_with_glean(move |glean| metric.record(glean, timestamp, Some(extra)));
    }
}

#[inherent(pub)]
impl<K: traits::ExtraKeys> traits::Event for EventMetric<K> {
    type Extra = K;

    fn record<M: Into<Option<<Self as traits::Event>::Extra>>>(&self, extra: M) {
        let now = crate::get_timestamp_ms();

        // Translate from {ExtraKey -> String} to a [Int -> String] map
        let extra = extra.into().map(|e| e.into_ffi_extra());
        let metric = Arc::clone(&self.inner);
        crate::launch_with_glean(move |glean| metric.record(glean, now, extra));
    }

    fn test_get_value<'a, S: Into<Option<&'a str>>>(
        &self,
        ping_name: S,
    ) -> Option<Vec<RecordedEvent>> {
        crate::block_on_dispatcher();

        let queried_ping_name = ping_name
            .into()
            .unwrap_or_else(|| &self.inner.meta().send_in_pings[0]);

        crate::with_glean(|glean| self.inner.test_get_value(glean, queried_ping_name))
    }

    fn test_get_num_recorded_errors<'a, S: Into<Option<&'a str>>>(
        &self,
        error: ErrorType,
        ping_name: S,
    ) -> i32 {
        crate::block_on_dispatcher();

        crate::with_glean_mut(|glean| {
            glean_core::test_get_num_recorded_errors(
                glean,
                self.inner.meta(),
                error,
                ping_name.into(),
            )
            .unwrap_or(0)
        })
    }
}

#[cfg(test)]
mod test {
    use super::*;
    use crate::common_test::{lock_test, new_glean};
    use crate::CommonMetricData;

    #[test]
    fn no_extra_keys() {
        let _lock = lock_test();
        let _t = new_glean(None, true);

        let metric: EventMetric<NoExtraKeys> = EventMetric::new(CommonMetricData {
            name: "event".into(),
            category: "test".into(),
            send_in_pings: vec!["test1".into()],
            ..Default::default()
        });

        metric.record(None);
        metric.record(None);

        let data = metric.test_get_value(None).expect("no event recorded");
        assert_eq!(2, data.len());
        assert!(data[0].timestamp <= data[1].timestamp);
    }

    #[test]
    fn with_extra_keys() {
        let _lock = lock_test();
        let _t = new_glean(None, true);

        #[derive(Default, Debug, Clone, Hash, Eq, PartialEq)]
        struct SomeExtra {
            key1: Option<String>,
            key2: Option<String>,
        }

        impl glean_core::traits::ExtraKeys for SomeExtra {
            const ALLOWED_KEYS: &'static [&'static str] = &["key1", "key2"];

            fn into_ffi_extra(self) -> HashMap<i32, String> {
                let mut map = HashMap::new();
                self.key1.and_then(|key1| map.insert(0, key1));
                self.key2.and_then(|key2| map.insert(1, key2));
                map
            }
        }

        let metric: EventMetric<SomeExtra> = EventMetric::new(CommonMetricData {
            name: "event".into(),
            category: "test".into(),
            send_in_pings: vec!["test1".into()],
            ..Default::default()
        });

        let map1 = SomeExtra {
            key1: Some("1".into()),
            ..Default::default()
        };
        metric.record(map1);

        let map2 = SomeExtra {
            key1: Some("1".into()),
            key2: Some("2".into()),
        };
        metric.record(map2);

        metric.record(None);

        let data = metric.test_get_value(None).expect("no event recorded");
        assert_eq!(3, data.len());
        assert!(data[0].timestamp <= data[1].timestamp);
        assert!(data[1].timestamp <= data[2].timestamp);

        let mut map = HashMap::new();
        map.insert("key1".into(), "1".into());
        assert_eq!(Some(map), data[0].extra);

        let mut map = HashMap::new();
        map.insert("key1".into(), "1".into());
        map.insert("key2".into(), "2".into());
        assert_eq!(Some(map), data[1].extra);

        assert_eq!(None, data[2].extra);
    }
}
