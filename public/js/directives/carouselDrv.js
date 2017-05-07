(function () {
    angular.module('myApp').directive('carousel', [function() {
        return {
            restrict: 'E',
            templateUrl:'/js/directives/carouselDrv.html',
            replace: true,
            scope: {
                postObject: '='
            }
        };
    }]);
})();
