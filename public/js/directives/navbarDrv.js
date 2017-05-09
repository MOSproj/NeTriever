(function () {
    angular.module('myApp').directive('navbar', function() {
        return {
            restrict: 'E',
            templateUrl:'/js/directives/navbarDrv.html',
            replace: true,
            scope: {
                categories: '='
            }
        };
    });
})();
