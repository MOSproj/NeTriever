(function () {
    angular.module('myApp').filter('isNumber', [ '$filter', function($filter) {
        return function (data) {
            var intData = parseInt(data);
            if (data === intData && (intData > 2017 || intData < 1970))
                return $filter('number')(data);
            return data;
        }
    }]);
})();
