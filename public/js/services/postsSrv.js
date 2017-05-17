(function(){
    "use strict";

    angular.module('myApp').factory("postsSrv", ["$http", "$log" , postsSrv]);

    function postsSrv($http, $log){
        return {
            getPostsByCategory: function(categoryId, reqParams){
                return $http.get('/api/posts/' + categoryId, {
                    params: reqParams
                });
            },
            getPostsByIds: function(ids){
                return $http.get('/api/postsIds/' + ids);
            }
        };
    }
})();
