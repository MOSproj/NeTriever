(function () {
    angular.module('myApp').directive('specSelect', function() {
        return {
            restrict: 'E',
            templateUrl:'/js/directives/specSelectDrv.html',
            replace: true,
            scope: {
            },
            link: function($scope, $el) {
                $('.selectpicker').selectpicker();
            }
        };
    });
})();
