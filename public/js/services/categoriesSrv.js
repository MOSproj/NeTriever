(function(){
    "use strict";

    angular.module('myApp').factory("categoriesSrv", ["$http", "$log" , categoriesSrv]);

    function categoriesSrv($http,$log){
        var cache = null;

        if (cache == null)
            return {
                getCategories : function(){
                    return $http.get('/get-categories');
                }
            };
        else return cache;
    }
})();
