(function(){
    "use strict";

    angular.module('myApp').factory("categoriesServices", ["$http", "$log" , categoriesServices]);

    function categoriesServices($http,$log){
        var cache = null;

        if (cache == null)
            return {
                getCategories : function(){
                    return $http.get('/categories');
                },
                getCategory : function(name){
                    return $http.get('/categories/:name');
                }
            };
        else return cache;
    }
})();
