(function () {
    angular.module('myApp').directive('specRange', function() {
        return {
            restrict: 'E',
            templateUrl:'js/directives/specRangeDrv.html',
            replace: true,
            scope: {
                specKey: '=',
                specValMin: '=',
                specValMax: '=',
                specModelMin: '=',
                specModelMax: '='
            }
        };
    });
})();
