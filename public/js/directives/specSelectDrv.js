(function () {
    angular.module('myApp').directive('specSelect', function() {
        return {
            restrict: 'E',
            templateUrl:'/js/directives/specSelectDrv.html',
            replace: true,
            scope: {
                // TODO: change that
                specKey: '=',
                specVal: '=',
                settings: '='
            }
        };
    });
})();
