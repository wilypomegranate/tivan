(function() {
  'use strict';

  angular
    .module('materialUi')
    .config(routerConfig);

  /** @ngInject */
  function routerConfig($stateProvider, $urlRouterProvider) {
    $stateProvider
      .state('home', {
        url: '/',
        templateUrl: 'app/main/main.html',
        controller: 'MainController',
        controllerAs: 'main'
      })
      .state('camera', {
        url: '/camera',
        templateUrl: 'app/camera/camera.html',
        controller: 'CameraController',
        controllerAs: 'camera'
      });

    $urlRouterProvider.otherwise('/');
  }

})();
