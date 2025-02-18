import pytest
from tripservice.tripservice import (
    Trip, User, TestUserSession, 
    TestTripRepository, TripService,
    UserNotLoggedInException
)

def test_get_trips_by_user():
    # Arrange
    logged_user = User()
    target_user = User()
    target_user.addFriend(logged_user)
    expected_trips = [Trip(), Trip()]
    
    user_session = TestUserSession(logged_user)
    trip_repository = TestTripRepository(expected_trips)
    trip_service = TripService(user_session, trip_repository)
    
    # Act
    trips = trip_service.get_trips_by_user(target_user)
    
    # Assert
    assert trips == expected_trips

def test_get_trips_unauthorized_user():
    # Arrange
    logged_user = User()
    target_user = User()  # not friends
    
    user_session = TestUserSession(logged_user)
    trip_repository = TestTripRepository([Trip()])
    trip_service = TripService(user_session, trip_repository)
    
    # Act
    trips = trip_service.get_trips_by_user(target_user)
    
    # Assert
    assert trips == []

def test_get_trips_not_logged_in():
    # Arrange
    user_session = TestUserSession(None)  # no logged in user
    trip_service = TripService(user_session, TestTripRepository())
    
    # Act/Assert
    with pytest.raises(UserNotLoggedInException):
        trip_service.get_trips_by_user(User())