(function () {
    angular.module('myApp').filter('calculatedDate', function() {
        return function (time) {
            var startDate = new Date(time);
            var endDate = new Date();
            var minutes = (Math.floor((endDate - startDate) / (1000 * 60)) % 60).toLocaleString(undefined, {minimumIntegerDigits: 1});
            var hours = Math.floor((endDate - startDate) / (1000 * 60 * 60)).toLocaleString(undefined, {minimumIntegerDigits: 1});

            if (hours < 1) {
                if (minutes <2)
                    return "לפני דקה";
                return "לפני " + minutes + " דקות";
            }
            if (hours < 24) {
                if (hours < 2)
                    return "לפני שעה";
                if (hours < 3)
                    return "לפני שעתיים";
                return "לפני " + hours + " שעות";
            }

            var months = ['', 'ינואר', 'פבואר', 'מרץ', 'אפריל', 'מאי', 'יוני', 'יולי', 'אוגוסט', 'ספטמבר', 'אוקטובר', 'נובמבר', 'דצמבר'];
            return dateToReturn = (time.slice(8, 10) + " " + months[parseInt(time.slice(5, 7), 10)] + ", " + time.slice(0, 4));
        }
    });
})();