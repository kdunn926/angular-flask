'use strict';

angular.module('EducationUnited', ['angularFlaskServices'])
	.config(['$routeProvider', '$locationProvider',
		function($routeProvider, $locationProvider) {
		$routeProvider
		.when('/', {
			templateUrl: 'static/partials/index.html',
			controller: IndexController
		})
		.when('/mission', {
			templateUrl: 'static/partials/mission.html',
			controller: AboutController
		})
		.when('/projects', {
			templateUrl: 'static/partials/projects.html',
			controller: AboutController
		})
		.when('/people', {
			templateUrl: 'static/partials/people.html',
			controller: AboutController
		})
		.otherwise({
			redirectTo: '/'
		})
		;

		$locationProvider.html5Mode(true);
	}])
;
