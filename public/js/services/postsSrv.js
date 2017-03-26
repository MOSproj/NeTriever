(function(){
    "use strict";

    angular.module('myApp').factory("postsSrv", ["$http", "$log" , postsSrv]);

    function postsSrv($http, $log){
        return {
            getPosts : function(category){
                return $http.get('/api/posts/' + category);
            }
        };
    }
})();
