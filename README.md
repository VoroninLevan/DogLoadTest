# DogLoadTest code challenge

This is an app to load test some endpoints of 'Dog API' web site. Uses **Locust** as framework.

### Tests:
* SequentialTaskSet:
  * `perform_listing()` - '*List all breeds*' endpoint test. Also retreives and saves JSON response as dict. First task of **SequentialTaskSet**
  * `perform_listing_by_breed()` - '*By breed*' endpoint test. Uses data retreived in `perform_listing()` for listing. Second task of **SequentialTaskSet**
* `random_image()` - '*Random image*' endpoint test

### Parameters
`locust.conf` used to configure the run. Following parameters in place at the moment, more can be added:
* **General**
  * `locustfile` - **locustfile.py** location
  * `host` - host under test, e.g. '*http://example.com*'
* **User settings**
  * `users` - amount of users to be spawned, e.g. '*10*'
  * `hatch-rate` - user hatching(spawn) rate in seconds, e.g. '*5*'
* **Headless mode settings**
  * `headless` - accepts '*true*' or '*false*' values. Used to identify non-UI/UI run
  * `run-time` - run length in format '*hms*', e.g. '*30m*'. NOTE: should be commented if `headless` set to '*false*'
* **Step settings**
  * `step-load` - accepts '*true*' or '*false*' values. Used to identify step-load mode
  * `step-users` - amount of users to be hatched(spawned) on step, e.g. '*5*'. Works together with `step-load`
  * `step-time` - length of one step in format '*hms*', e.g. '*10s*'. Works together with `step-load`
* **Reporting**
  * `csv` - accepts '*true*' or '*false*' values. Three reports would be create if enabled('*true*')
  
NOTE: in order to run the app - **Locust** should be installed on machine and be in a system path. Alternitevely virtual environment might be used.
Might be installed with `pip3 install locust`
