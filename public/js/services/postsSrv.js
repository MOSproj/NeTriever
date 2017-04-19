(function(){
    "use strict";

    angular.module('myApp').factory("postsSrv", ["$http", "$log" , postsSrv]);

    function postsSrv($http, $log){
        return {
            getPosts : function(category, reqParams){
                return $http.get('/api/category/' + category, {
                    params: reqParams
                });
            }
        };
    }
})();
