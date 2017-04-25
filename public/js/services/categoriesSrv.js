(function(){
    "use strict";

    angular.module('myApp').factory("categoriesSrv", ["$http", "$log" , categoriesSrv]);

    function categoriesSrv($http, $log){
        return {
            getCategories : function(){
                return $http.get('/api/categories');
            },
            getCategoriesNames : function(){
                return $http.get('/api/categories-names');
            },
            getCategory : function(categoryId){
                return $http.get('/api/category/' + categoryId);
            }
        };
    }
})();
