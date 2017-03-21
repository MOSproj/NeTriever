(function(){
    "use strict";

    angular.module('myApp').factory("postsSrv", ["$http", "$log" , postsSrv]);

    function postsSrv($http,$log){
        var cache = null;

        if (cache == null)
            return {
                getPosts : function(category){
                    return $http.get('/get-posts/' + category);
                }
            };
        else return cache;
    }
})();
