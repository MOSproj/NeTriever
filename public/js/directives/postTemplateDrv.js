(function () {
    angular.module('myApp').directive('postTemplate', [function() {
        return {
            restrict: 'E',
            scope: {
                info: '='
            },
            templateUrl:'/js/directives/postTemplateDrv.html',
            replace: true
        };
    }]);
})();
