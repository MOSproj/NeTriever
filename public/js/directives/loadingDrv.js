(function () {
    angular.module('myApp').directive('loading', function() {
        return {
            restrict: 'E',
            templateUrl:'/js/directives/loadingDrv.html',
            replace: true,
            scope: {
            }
        };
    });
})();
