(function () {
    angular.module('myApp').directive('specSelect', function() {
        return {
            restrict: 'E',
            templateUrl:'/js/directives/specSelectDrv.html',
            replace: true,
            link: function($scope, $el) {
                $('.selectpicker').selectpicker();
            },
            scope: {
            }
        };
    });
})();
