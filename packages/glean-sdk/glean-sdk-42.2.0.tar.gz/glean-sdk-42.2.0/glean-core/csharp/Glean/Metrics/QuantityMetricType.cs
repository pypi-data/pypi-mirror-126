// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at http://mozilla.org/MPL/2.0/.

using Mozilla.Glean.FFI;
using System;

namespace Mozilla.Glean.Private
{
    /// <summary>
    /// This implements the developer facing API for recording quantity metrics.
    /// 
    /// Instances of this class type are automatically generated by the parsers at build time,
    /// allowing developers to record values that were previously registered in the metrics.yaml file.
    ///
    /// The quantity API only exposes the [set] method.
    //
    /// </summary>
    public sealed class QuantityMetricType {
        private bool disabled;
        private string[] sendInPings;
        private UInt64 handle;

        /// <summary>
        /// The public constructor used by automatically generated metrics.
        /// </summary>
        public QuantityMetricType(
            bool disabled,
            string category,
            Lifetime lifetime,
            string name,
            string[] sendInPings
            ) : this(0, disabled, sendInPings)
        {
            handle = LibGleanFFI.glean_new_quantity_metric(
                    category: category,
                    name: name,
                    send_in_pings: sendInPings,
                    send_in_pings_len: sendInPings.Length,
                    lifetime: (int)lifetime,
                    disabled: disabled);
        }

        internal QuantityMetricType(
            UInt64 handle,
            bool disabled,
            string[] sendInPings
            )
        {
            this.disabled = disabled;
            this.sendInPings = sendInPings;
            this.handle = handle;
        }


        /// <summary>
        /// Set a quantity value.
        /// </summary>
        /// <param name="value">The value to set. Must be non-negative.</param>
        public void Set(Int32 value)
        {
            if (disabled)
            {
                return;
            }

            Dispatchers.LaunchAPI(() => {
                LibGleanFFI.glean_quantity_set(this.handle, value);
            });
        }


        /// <summary>
        /// Tests whether a value is stored for the metric for testing purposes only. This function will
        /// attempt to await the last task (if any) writing to the the metric's storage engine before
        /// returning a value.
        /// </summary>
        /// <param name="pingName">represents the name of the ping to retrieve the metric for Defaults
        /// to the first value in `sendInPings`</param>
        /// <returns>true if metric value exists, otherwise false</returns>
        public bool TestHasValue(string pingName = null)
        {
            Dispatchers.AssertInTestingMode();

            string ping = pingName ?? sendInPings[0];
            return LibGleanFFI.glean_quantity_test_has_value(this.handle, ping);
        }

        /// <summary>
        /// Returns the stored value for testing purposes only. This function will attempt to await the
        /// last task (if any) writing to the the metric's storage engine before returning a value.
        /// @throws [NullPointerException] if no value is stored
        /// </summary>
        /// <param name="pingName">represents the name of the ping to retrieve the metric for.
        /// Defaults to the first value in `sendInPings`</param>
        /// <returns>value of the stored metric</returns>
        /// <exception cref="System.NullReferenceException">Thrown when the metric contains no value</exception>
        public Int32 TestGetValue(string pingName = null)
        {
            Dispatchers.AssertInTestingMode();

            if (!TestHasValue(pingName))
            {
                throw new NullReferenceException();
            }

            string ping = pingName ?? sendInPings[0];
            return LibGleanFFI.glean_quantity_test_get_value(this.handle, ping);
        }

        /// <summary>
        /// Returns the number of errors recorded for the given metric.
        /// </summary>
        /// <param name="errorType">the type of the error recorded.</param>
        /// <param name="pingName">represents the name of the ping to retrieve the metric for.
        /// Defaults to the first value in `sendInPings`.</param>
        /// <returns>the number of errors recorded for the metric.</returns>
        public Int32 TestGetNumRecordedErrors(Testing.ErrorType errorType, string pingName = null)
        {
            Dispatchers.AssertInTestingMode();

            string ping = pingName ?? sendInPings[0];
            return LibGleanFFI.glean_quantity_test_get_num_recorded_errors(
                handle, (int)errorType, ping
            );
        }
    }
}
