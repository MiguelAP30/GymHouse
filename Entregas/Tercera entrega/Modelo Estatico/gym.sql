-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 19-03-2024 a las 07:32:36
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `gym`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Exercises`
--

CREATE TABLE `Exercises` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `video` varchar(100) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `dateAdded` date NOT NULL DEFAULT current_timestamp(),
  `rate` int(11) NOT NULL,
  `muscle` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ExercisesPerWeekDays`
--

CREATE TABLE `ExercisesPerWeekDays` (
  `id` int(11) NOT NULL,
  `exerciseID` int(11) NOT NULL,
  `weekDayID` int(11) NOT NULL,
  `routineID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Roles`
--

CREATE TABLE `Roles` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `RoutineExercises`
--

CREATE TABLE `RoutineExercises` (
  `id` int(11) NOT NULL,
  `exerciseID` int(11) NOT NULL,
  `routineID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Routines`
--

CREATE TABLE `Routines` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `RoutineUser`
--

CREATE TABLE `RoutineUser` (
  `id` int(11) DEFAULT NULL,
  `userID` varchar(60) NOT NULL,
  `routineID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Users`
--

CREATE TABLE `Users` (
  `email` varchar(60) NOT NULL,
  `name` varchar(60) NOT NULL,
  `lastname` varchar(60) NOT NULL,
  `id` varchar(10) NOT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `address` varchar(60) DEFAULT NULL,
  `password` varchar(20) NOT NULL,
  `roleID` int(11) NOT NULL,
  `lastPayment` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `WeekDays`
--

CREATE TABLE `WeekDays` (
  `id` int(11) NOT NULL,
  `name` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `Exercises`
--
ALTER TABLE `Exercises`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `ExercisesPerWeekDays`
--
ALTER TABLE `ExercisesPerWeekDays`
  ADD PRIMARY KEY (`id`),
  ADD KEY `exerciseID` (`exerciseID`),
  ADD KEY `weekDayID` (`weekDayID`),
  ADD KEY `routineID` (`routineID`);

--
-- Indices de la tabla `Roles`
--
ALTER TABLE `Roles`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `RoutineExercises`
--
ALTER TABLE `RoutineExercises`
  ADD PRIMARY KEY (`id`),
  ADD KEY `exerciseID` (`exerciseID`),
  ADD KEY `routineID` (`routineID`);

--
-- Indices de la tabla `Routines`
--
ALTER TABLE `Routines`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `RoutineUser`
--
ALTER TABLE `RoutineUser`
  ADD KEY `userID` (`userID`),
  ADD KEY `routineID` (`routineID`);

--
-- Indices de la tabla `Users`
--
ALTER TABLE `Users`
  ADD PRIMARY KEY (`email`),
  ADD UNIQUE KEY `id` (`id`),
  ADD KEY `status` (`roleID`);

--
-- Indices de la tabla `WeekDays`
--
ALTER TABLE `WeekDays`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `Exercises`
--
ALTER TABLE `Exercises`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `ExercisesPerWeekDays`
--
ALTER TABLE `ExercisesPerWeekDays`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `Roles`
--
ALTER TABLE `Roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `RoutineExercises`
--
ALTER TABLE `RoutineExercises`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `Routines`
--
ALTER TABLE `Routines`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `WeekDays`
--
ALTER TABLE `WeekDays`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `ExercisesPerWeekDays`
--
ALTER TABLE `ExercisesPerWeekDays`
  ADD CONSTRAINT `exercisesperweekdays_ibfk_1` FOREIGN KEY (`exerciseID`) REFERENCES `Exercises` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `exercisesperweekdays_ibfk_2` FOREIGN KEY (`weekDayID`) REFERENCES `WeekDays` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `exercisesperweekdays_ibfk_3` FOREIGN KEY (`routineID`) REFERENCES `Routines` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `RoutineExercises`
--
ALTER TABLE `RoutineExercises`
  ADD CONSTRAINT `routineexercises_ibfk_1` FOREIGN KEY (`exerciseID`) REFERENCES `Exercises` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `routineexercises_ibfk_2` FOREIGN KEY (`routineID`) REFERENCES `Routines` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `RoutineUser`
--
ALTER TABLE `RoutineUser`
  ADD CONSTRAINT `routineuser_ibfk_1` FOREIGN KEY (`routineID`) REFERENCES `Routines` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `routineuser_ibfk_2` FOREIGN KEY (`userID`) REFERENCES `Users` (`email`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `Users`
--
ALTER TABLE `Users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`roleID`) REFERENCES `Roles` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
