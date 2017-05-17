(function(){
    "use strict";

    angular.module('myApp').config(['$routeProvider', '$locationProvider', routing]);

    function routing($routeProvider, $locationProvider) {
        $routeProvider
            .when("/", {
                templateUrl : "/views/home.html"
            })
            .when("/category/:categoryId", {
                controller: 'postsCtrl',
                controllerAs:"posts",
                templateUrl : "/views/category.html"
            })
            .when("/מועדפים", {
                controller: 'likesCtrl',
                controllerAs:"likes",
                templateUrl : "/views/likes.html"
            })
            .when("/404", {
                templateUrl : "/views/404.html"
            })
            .otherwise({
                redirectTo: '/404'
            });

        $locationProvider.hashPrefix('');
        $locationProvider.html5Mode(true);
    }
})();
