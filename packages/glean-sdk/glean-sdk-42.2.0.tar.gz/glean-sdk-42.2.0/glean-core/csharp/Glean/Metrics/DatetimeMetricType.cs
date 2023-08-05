﻿// This Source Code Form is subject to the terms of the Mozilla Public
// License, v. 2.0. If a copy of the MPL was not distributed with this
// file, You can obtain one at http://mozilla.org/MPL/2.0/.

using System;
using Mozilla.Glean.FFI;
using System.Globalization;

namespace Mozilla.Glean.Private
{
    /// <summary>
    /// This implements the developer facing API for recording datetime metrics.
    ///
    /// Instances of this class type are automatically generated by the parsers at build time,
    /// allowing developers to record values that were previously registered in the metrics.yaml file.
    /// </summary>
    public sealed class DatetimeMetricType
    {
        private bool disabled;
        private string[] sendInPings;
        private UInt64 handle;

        /// <summary>
        /// The public constructor used by automatically generated metrics.
        /// </summary>
        public DatetimeMetricType(
            bool disabled,
            string category,
            Lifetime lifetime,
            string name,
            string[] sendInPings,
            TimeUnit timeUnit = TimeUnit.Minute
            ) : this(0, disabled, sendInPings)
        {
            handle = LibGleanFFI.glean_new_datetime_metric(
                       category: category,
                       name: name,
                       send_in_pings: sendInPings,
                       send_in_pings_len: sendInPings.Length,
                       lifetime: (int)lifetime,
                       disabled: disabled,
                       time_unit: (int)timeUnit);
        }

        internal DatetimeMetricType(
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
        /// Set a datetime value, truncating it to the metric's resolution.
        /// </summary>
        /// <param name="value"> The [Date] value to set. If not provided, will record the current time.
        public void Set(DateTimeOffset value = new DateTimeOffset())
        {
            if (disabled)
            {
                return;
            }
            // The current time of datetime offset.
            var currentTime = value.DateTime;
            // InvariantCulture calendar still preserves timezones and locality information,
            // it just formats them in a way to ease persistence.
            var calendar = CultureInfo.InvariantCulture.Calendar;

            Dispatchers.LaunchAPI(() => {
                LibGleanFFI.glean_datetime_set(
                    handle,
                    year: calendar.GetYear(currentTime),
                    month: calendar.GetMonth(currentTime),
                    day: calendar.GetDayOfMonth(currentTime),
                    hour: calendar.GetHour(currentTime),
                    minute: calendar.GetMinute(currentTime),
                    second: calendar.GetSecond(currentTime),
                    nano: Convert.ToInt64(1000000 * calendar.GetMilliseconds(currentTime)),
                    offset_seconds: Convert.ToInt32((currentTime - value.UtcDateTime).TotalSeconds)
                );;
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
            return LibGleanFFI.glean_datetime_test_has_value(this.handle, ping) != 0;
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
        public string TestGetValueAsString(string pingName = null)
        {
            Dispatchers.AssertInTestingMode();

            string ping = pingName ?? sendInPings[0];
            if (!TestHasValue(ping))
            {
                throw new NullReferenceException();
            }

            return LibGleanFFI.glean_datetime_test_get_value_as_string(this.handle, ping).AsString();
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
        public DateTimeOffset TestGetValue(string pingName = null)
        {
            return DateTimeOffset.Parse(TestGetValueAsString(pingName));
        }

        /**
         * Returns the number of errors recorded for the given metric.
         *
         * @param errorType The type of the error recorded.
         * @param pingName represents the name of the ping to retrieve the metric for.
         *                 Defaults to the first value in `sendInPings`.
         * @return the number of errors recorded for the metric.
         */
        public Int32 TestGetNumRecordedErrors(Testing.ErrorType errorType, string pingName = null)
        {
            Dispatchers.AssertInTestingMode();

            string ping = pingName ?? sendInPings[0];
            return LibGleanFFI.glean_datetime_test_get_num_recorded_errors(
                this.handle, (int)errorType, ping
            );
        }
    }
}
