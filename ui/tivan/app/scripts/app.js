'use strict';

/**
 * @ngdoc overview
 * @name tivanApp
 * @description
 * # tivanApp
 *
 * Main module of the application.
 */
angular
  .module('tivanApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl',
        controllerAs: 'main'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl',
        controllerAs: 'about'
      })
      .otherwise({
        redirectTo: '/'
      });
  })
  .config(function ($sceDelegateProvider) {
    $sceDelegateProvider.resourceUrlWhitelist([
    // Allow same origin resource loads.
    'self'
    ]);
  });
