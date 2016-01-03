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
      })
      .state('camera_select', {
        url: '/camera_select',
        templateUrl: 'app/camera_select/camera_select.html',
        controller: 'CameraSelectController',
        controllerAs: 'camera_select'
      });

    $urlRouterProvider.otherwise('/');
  }

})();
