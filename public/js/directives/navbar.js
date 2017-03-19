(function () {
    angular.module('myApp').directive('navbar', function() {
        return {
            restrict: 'E',
            scope: {
                info: '='
            },
            templateUrl:'js/directives/navbar.html'
        };
    });
})();
