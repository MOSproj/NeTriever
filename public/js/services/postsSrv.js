(function(){
    "use strict";

    angular.module('myApp').factory("postsSrv", ["$http", "$log" , postsSrv]);

    function postsSrv($http, $log){
        return {
            getPosts : function(categoryId, reqParams){
                return $http.get('/api/posts/' + categoryId, {
                    params: reqParams
                });
            }
        };
    }
})();
