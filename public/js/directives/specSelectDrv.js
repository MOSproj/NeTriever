(function () {
    angular.module('myApp').directive('specSelect', function() {
        return {
            restrict: 'E',
            scope: {
                info: '='
            },
            templateUrl:'/js/directives/specSelectDrv.html',
            link: function($scope, $el) {
                $('.selectpicker').selectpicker();
            }
        };
    });
})();
