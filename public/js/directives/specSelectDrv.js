(function () {
    angular.module('myApp').directive('specSelect', function() {
        return {
            restrict: 'E',
            scope: {
                info: '='
            },
            templateUrl:'/js/directives/specSelectDrv.html',
            replace: true,
            link: function($scope, $el) {
                $('.selectpicker').selectpicker();
            }
        };
    });
})();
