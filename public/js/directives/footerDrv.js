(function () {
    angular.module('myApp').directive('footerDrv', [function() {
        return {
            restrict: 'E',
            templateUrl:'/js/directives/footerDrv.html',
            replace: true,
            scope: {
                categories: '='
            },
            link: function () {
                angular.element('body')[0].style.paddingBottom =
                    angular.element('footer')[0].offsetHeight + 60 + 30 + 'px';
            }
        };
    }]);
})();
