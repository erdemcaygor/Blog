
var blgApp = angular.module('blgApp',['ngDisqus']);


blgApp.config(function($routeProvider, $httpProvider, $disqusProvider, $locationProvider){

    $locationProvider.hashPrefix('!');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $disqusProvider.setShortname('erdemcaygor.com');
    $httpProvider.defaults.headers.common['X-CSRFToken'] = '{{ csrf_token|escapejs }}';
    $routeProvider
        .when('/',{
            cache:false,
            controller:'home',
            templateUrl:'static/app/partial/home.html'
        })
        .when('/kategori/:category_name/',{
            controller:'category',
            templateUrl:'static/app/partial/category.html'
        })
        .when('/post/:slug/',{
            cache:false,
            controller:'post',
            templateUrl:'static/app/partial/post.html'
        })
        .when('/iletisim/',{
            controller:'iletisim',
            templateUrl:'static/app/partial/iletisim.html'
        })
        .when('/tag/:slug/',{
            controller:'tag',
            templateUrl:'static/app/partial/tag.html'
        })
        .otherwise({redirectTo:'/'});

});














