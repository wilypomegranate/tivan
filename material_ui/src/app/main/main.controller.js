(function() {
  'use strict';

  angular
    .module('materialUi')
    .controller('MainController', MainController);

  /** @ngInject */
  function MainController($timeout, $http, $log) {
    var vm = this;

    $http.get('/api/events/').success(function(data){
        vm.events = data;
    });

    vm.getVideoFromEvent = function(event_id) {
        $log.info('here');
        return '/api/video/retrieval/' + event_id + '/';
    }

    vm.getVideoFromEvent(1);
 
  }
})();
