blgApp.factory('blgFactory', function ($http, $q) {

    var posts_url = '/api/posts/';
    var categories_url = '/api/categories/';
    var categoryPosts_url = '/api/category-posts/';
    var postDetail_url = '/api/post/';
    var taggedPosts_url = '/api/tag/';
    var posttags_url = '/api/posttags/';
    var search_url = '/api/search/';
    var mail_url = '/api/mail/';
    var factory = {};

    factory.getPosts = function () {

        var deferer = $q.defer();

        $http.get(posts_url)
            .success(function (data) {

                deferer.resolve(data);
            })
            .error(function (data) {

                deferer.reject('bir hata oluştu');
            });
        return deferer.promise;
    };

    factory.getCategories = function () {

        var deferer = $q.defer();

        $http.get(categories_url)
            .success(function (data) {

                deferer.resolve(data);
            })
            .error(function () {

                deferer.reject('bir hata oluştu');
            });

        return deferer.promise;
    };

    factory.getCategoryPosts = function (category_name) {

        var deferer = $q.defer();

        $http.get(categoryPosts_url + category_name + '/')

            .success(function (data) {

                deferer.resolve(data);
            })
            .error(function () {

                deferer.reject('bir hata oluştu');
            });

        return deferer.promise;
    };


    factory.getPostDetail = function (slug) {

        var deferer = $q.defer();
        $http.get(postDetail_url + slug + '/')
            .success(function (data) {
                deferer.resolve(data);
            })
            .error(function () {
                deferer.reject('bir hata oluştu');
            });
        return deferer.promise;
    };

    factory.getTaggedPosts = function (slug) {

        var deferer = $q.defer();

        $http.get(taggedPosts_url + slug + '/')
            .success(function (data) {
                deferer.resolve(data);
            })
            .error(function () {
                deferer.reject('bir hata oluştu');
            });

        return deferer.promise;
    };

    factory.getPostTags = function(slug){

        var deferer = $q.defer();
        $http.get(posttags_url+slug+'/')
            .success(function(data){

                deferer.resolve(data);
            })
            .error(function(){
                deferer.reject("hata");
            });
        return deferer.promise;
    };

    factory.search = function(search_data){

        var deferer = $q.defer();
        $http.get(search_url, {params:{search_data:search_data}})
            .success(function(data){
                console.log(data);
                deferer.resolve(data);
            })
            .error(function(){
                deferer.reject("hata!");
            });

        return deferer.promise;
    };

    factory.mail = function(message){

        var deferer = $q.defer();

        $http.post(mail_url,{message:message})

            .success(function(data, status){

                deferer.resolve(status);
            })
            .error(function(data,status){

                deferer.resolve(status);
            });

        return deferer.promise;
    };

    return factory;
});


