blgApp.controller('home', function ($scope, blgFactory) {

    blgFactory.getPosts().then(function (data) {

        $scope.posts = data;

    });

    blgFactory.getCategories().then(function (data) {

        $scope.categories = data;
    });

    $scope.$watch('search_data', function () {

        var search_data = $scope.search_data;
        if (search_data) {
            $('#maincontainer').addClass('search-style');
            blgFactory.search(search_data).then(function (data) {

                $scope.posts = data;
                $('#maincontainer').removeClass('search-style');
            });
        }

    });

});


blgApp.controller('category', function ($scope, $routeParams, blgFactory, $location) {

    var name = $routeParams.category_name;

    if (name) {
        blgFactory.getCategoryPosts(name).then(function (data) {

            $scope.posts = data;
        });

    } else {
        $location.path('/');
    }


});


blgApp.controller('post', function ($scope, $routeParams, blgFactory) {

    var slug = $routeParams.slug;
    blgFactory.getPostDetail(slug).then(function (data) {
        console.log(data);
        $scope.post = data;
        $('#content').html($scope.post.content);

    });

    blgFactory.getPostTags(slug).then(function (data) {

        $scope.tags = data;
    });

});


blgApp.controller('iletisim', function ($scope, blgFactory) {

    $scope.send = function () {
        var message = $scope.message;
        var submit_button = $('#contactForm button[type=submit]');
        submit_button.prop('disabled', true);
        blgFactory.mail(message).then(function (status) {

            if(status == '400'){

                swal('Hata!','mesaj gönderilemiyor, lütfen tekrar deneyiniz.','error');
                $scope.message = {};
                submit_button.prop('disabled', false);
            }
            if(status == '200'){
                swal('İşlem gerçekleştirildi', 'mesajınız başarıyla iletilmiştir', 'success');
                $scope.message = {};
                submit_button.prop('disabled', false);
            }
            if(status=='500'){
                submit_button.prop('disabled', false);
            }
        });
    }


});

blgApp.controller('tag', function ($scope, $routeParams, blgFactory) {

    var slug = $routeParams.slug;
    blgFactory.getTaggedPosts(slug).then(function (data) {

        $scope.posts = data;
    });

});












