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
                controller: 'lovesCtrl',
                controllerAs:"loves",
                templateUrl : "/views/loves.html"
            })
            .when("/עלינו", {
                controller: 'aboutCtrl',
                controllerAs:"about",
                templateUrl : "/views/about.html"
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
