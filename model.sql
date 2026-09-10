-- model.sql
-- Creates the AirBnB clone database schema from the ERD:
-- State, City, User, Place, Review, Amenity, PlaceAmenity.
-- Safe to run multiple times: the database and every table are
-- only created if they do not already exist.

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;

-- State: id, created_at, updated_at, name
CREATE TABLE IF NOT EXISTS states (
    id VARCHAR(60) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    name VARCHAR(128) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- City: id, created_at, updated_at, state_id (FK -> State), name
CREATE TABLE IF NOT EXISTS cities (
    id VARCHAR(60) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    state_id VARCHAR(60) NOT NULL,
    name VARCHAR(128) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- User: id, created_at, updated_at, email, password,
--       first_name (optional), last_name (optional)
CREATE TABLE IF NOT EXISTS users (
    id VARCHAR(60) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    email VARCHAR(128) NOT NULL,
    password VARCHAR(128) NOT NULL,
    first_name VARCHAR(128),
    last_name VARCHAR(128),
    PRIMARY KEY (id),
    UNIQUE (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Amenity: id, created_at, updated_at, name
CREATE TABLE IF NOT EXISTS amenities (
    id VARCHAR(60) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    name VARCHAR(128) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Place: id, created_at, updated_at, user_id (FK -> User), name,
--        city_id (FK -> City), description (optional),
--        number_rooms, number_bathrooms, max_guest, price_by_night
--        (all default 0), latitude (optional), longitude (optional)
CREATE TABLE IF NOT EXISTS places (
    id VARCHAR(60) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    user_id VARCHAR(60) NOT NULL,
    name VARCHAR(128) NOT NULL,
    city_id VARCHAR(60) NOT NULL,
    description VARCHAR(1024),
    number_rooms INT NOT NULL DEFAULT 0,
    number_bathrooms INT NOT NULL DEFAULT 0,
    max_guest INT NOT NULL DEFAULT 0,
    price_by_night INT NOT NULL DEFAULT 0,
    latitude FLOAT,
    longitude FLOAT,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (city_id) REFERENCES cities(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Review: id, created_at, updated_at, user_id (FK -> User),
--         place_id (FK -> Place), text
CREATE TABLE IF NOT EXISTS reviews (
    id VARCHAR(60) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    user_id VARCHAR(60) NOT NULL,
    place_id VARCHAR(60) NOT NULL,
    text VARCHAR(1024) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (place_id) REFERENCES places(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- PlaceAmenity: join table for the Place <-> Amenity many-to-many
-- relationship (amenity_id FK -> Amenity, place_id FK -> Place)
CREATE TABLE IF NOT EXISTS place_amenity (
    place_id VARCHAR(60) NOT NULL,
    amenity_id VARCHAR(60) NOT NULL,
    PRIMARY KEY (place_id, amenity_id),
    FOREIGN KEY (place_id) REFERENCES places(id) ON DELETE CASCADE,
    FOREIGN KEY (amenity_id) REFERENCES amenities(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
