/* This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/. */

import Foundation

typealias LabeledMetricCtor = (FfiStr?, FfiStr?, RawStringArray?, Int32, Int32, UInt8, RawStringArray?, Int32) -> UInt64

/// This implements the developer facing API for labeled metrics.
///
/// Instances of this class type are automatically generated by the parsers at build time,
/// allowing developers to record values that were previously registered in the metrics.yaml file.
///
/// Unlike most metric types, LabeledMetricType does not have its own corresponding storage engine,
/// but records metrics for the underlying metric type `T` in the storage engine for that type.
/// The only difference is that labeled metrics are stored with the special key `$category.$name/$label`.
public class LabeledMetricType<T> {
    let handle: UInt64
    let disabled: Bool
    let sendInPings: [String]
    let labels: Set<String>?
    let subMetric: T

    /// The public constructor used by automatically generated metrics.
    ///
    /// Supports the following types as sub-metrics:
    /// * `BooleanMetricType`
    /// * `CounterMetricType`
    /// * `StringMetricType`
    ///
    /// Throws an exception when used with unsupported sub-metrics.
    public init(
        category: String,
        name: String,
        sendInPings: [String],
        lifetime: Lifetime,
        disabled: Bool,
        subMetric: T,
        labels: Set<String>? = nil
    ) throws {
        self.disabled = disabled
        self.sendInPings = sendInPings
        self.labels = labels
        self.subMetric = subMetric

        var metricTypeInstantiator: LabeledMetricCtor
        switch subMetric {
        case is CounterMetricType:
            metricTypeInstantiator = glean_new_labeled_counter_metric
        case is BooleanMetricType:
            metricTypeInstantiator = glean_new_labeled_boolean_metric
        case is StringMetricType:
            metricTypeInstantiator = glean_new_labeled_string_metric
        default:
            throw "Can not create a labeled version of this metric type"
        }

        self.handle = withArrayOfCStrings(sendInPings) { pingArray in
            withArrayOfCStrings(labels?.sorted()) { labels in
                metricTypeInstantiator(
                    category,
                    name,
                    pingArray,
                    Int32(sendInPings.count),
                    lifetime.rawValue,
                    disabled.toByte(),
                    labels,
                    Int32(labels?.count ?? 0)
                )
            }
        }
    }

    /// Destroy this metric.
    deinit {
        if self.handle != 0 {
            switch self.subMetric {
            case is CounterMetricType:
                glean_destroy_labeled_counter_metric(self.handle)
            case is BooleanMetricType:
                glean_destroy_labeled_boolean_metric(self.handle)
            case is StringMetricType:
                glean_destroy_labeled_string_metric(self.handle)
            default:
                // Unreachable. The constructor will already throw an exception on an unhandled sub-metric type
                assertUnreachable()
            }
        }
    }

    /// Get the specific metric for a given label.
    ///
    /// If a set of acceptable labels was specified in the metrics.yaml file,
    /// and the given label is not in the set, it will be recorded under the
    /// special `OTHER_LABEL`.
    ///
    /// If a set of acceptable labels was not specified in the metrics.yaml file,
    /// only the first 16 unique labels will be used. After that, any additional
    /// labels will be recorded under the special `OTHER_LABEL` label.
    ///
    /// Labels must be snake_case and less than 30 characters. If an invalid label
    /// is used, the metric will be recorded in the special `OTHER_LABEL` label.
    ///
    /// - parameters:
    ///     * label: The label
    /// - returns: The specific metric for that label
    public subscript(label: String) -> T {
        // swiftlint:disable force_cast
        // REASON: We return the same type as the `subMetric` we match against

        switch self.subMetric {
        case is CounterMetricType:
            let handle = glean_labeled_counter_metric_get(self.handle, label)
            return CounterMetricType(withHandle: handle, disabled: self.disabled, sendInPings: self.sendInPings) as! T
        case is BooleanMetricType:
            let handle = glean_labeled_boolean_metric_get(self.handle, label)
            return BooleanMetricType(withHandle: handle, disabled: self.disabled, sendInPings: self.sendInPings) as! T
        case is StringMetricType:
            let handle = glean_labeled_string_metric_get(self.handle, label)
            return StringMetricType(withHandle: handle, disabled: self.disabled, sendInPings: self.sendInPings) as! T
        default:
            // The constructor will already throw an exception on an unhandled sub-metric type
            assertUnreachable()
        }
    }

    /// Returns the number of errors recorded for the given metric.
    ///
    /// - parameters:
    ///     * errorType: The type of the error recorded.
    ///     * pingName: represents the name of the ping to retrieve the metric for.
    ///                 Defaults to the first value in `sendInPings`.
    /// - returns: the number of errors recorded for the metric.
    public func testGetNumRecordedErrors(_ errorType: ErrorType, pingName: String? = nil) -> Int32 {
        Dispatchers.shared.assertInTestingMode()

        let pingName = pingName ?? self.sendInPings[0]

        switch self.subMetric {
        case is CounterMetricType:
            return glean_labeled_counter_test_get_num_recorded_errors(
                self.handle, errorType.rawValue, pingName
            )
        case is BooleanMetricType:
            return glean_labeled_boolean_test_get_num_recorded_errors(
                self.handle, errorType.rawValue, pingName
            )
        case is StringMetricType:
            return glean_labeled_string_test_get_num_recorded_errors(
                self.handle, errorType.rawValue, pingName
            )
        default:
            // The constructor will already throw an exception on an unhandled sub-metric type
            assertUnreachable()
        }
    }
}
