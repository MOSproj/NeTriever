(function(){
    "use strict";

    angular.module('myApp').factory("postsServices", ["$http", "$log" , postsServices]);

    function postsServices($http,$log){
        var cache = null;

        if (cache == null)
            return {
                /*getCategories : function(){
                    return $http.get('/categories');
                }*/
            };
        else return cache;
    }
})();
