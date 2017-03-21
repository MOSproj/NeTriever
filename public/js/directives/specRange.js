(function () {
    angular.module('myApp').directive('specRange', function() {
        return {
            restrict: 'E',
            scope: {
                info: '='
            },
            templateUrl:'js/directives/specRange.html'
        };
    });
})();
