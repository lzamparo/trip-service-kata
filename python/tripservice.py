#!/usr/bin/env python

class TripService:
  def __init__(self, user_session, trip_repository):
    self.user_session = user_session
    self.trip_repository = trip_repository

  def get_trips_by_user(self, user):
    logged_user = self.user_session.get_logged_user()
    if logged_user:
      if logged_user in user.getFriends():
        return self.trip_repository.find_trips_by_user(user)
      return [] 
    raise UserNotLoggedInException
  

class UserSession:
  def get_logged_user(self):
    raise DependendClassCallDuringUnitTestException(
      "Production user session being called in test"
    )
  
class TripRepository:
  def find_trips_by_user(self, user):
    raise DependendClassCallDuringUnitTestException(
      "Production trip repository being called in test"
    )


class TestUserSession(UserSession):
  def __init__(self, logged_user=None):
    self.logged_user = logged_user

  def get_logged_user(self):
    return self.logged_user
    
class TestTripRepository(TripRepository):
  def __init__(self, trips=None):
    self.trips = trips or []

  def find_trips_by_user(self, user):
    return self.trips
  


#
# Exceptions
#
class DependendClassCallDuringUnitTestException(Exception):
  pass

class UserNotLoggedInException(Exception):
  pass

#
# Classes
#
class Trip:
  pass

class User:
  def __init__(self):
    self.trips = []
    self.friends = []
  
  def addFriend(self, user):
    self.friends.append(user)
  
  def addTrip(self, trip):
    self.trips.append(trip)
  
  def getFriends(self):
    return self.friends
#
# Functions
#
def _isUserLoggedIn(user):
  raise DependendClassCallDuringUnitTestException(
    "_isUserLoggedIn() should not be called in an unit test"
  )

def _getLoggedUser():
  raise DependendClassCallDuringUnitTestException(
    "_getLoggedUser() should not be called in an unit test"
  )

def _findTripsByUser(user):
  raise DependendClassCallDuringUnitTestException(
    "_findTripsByUser() should not be invoked on an unit test."
  )

def getTripsByUser(user):
    loggedUser = _getLoggedUser()
    if loggedUser:
      if loggedUser in user.getFriends():
        return _findTripsByUser(user)
      else:
        return []
    else:
      raise UserNotLoggedInException()

if __name__ == "__main__":
  pass
