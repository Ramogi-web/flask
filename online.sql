-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 25, 2026 at 10:06 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `online`
--

-- --------------------------------------------------------

--
-- Table structure for table `active_wear`
--

CREATE TABLE `active_wear` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `brand` varchar(100) NOT NULL,
  `size` varchar(20) NOT NULL,
  `color` varchar(50) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `stock` int(11) NOT NULL,
  `photo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `active_wear`
--

INSERT INTO `active_wear` (`id`, `name`, `brand`, `size`, `color`, `gender`, `price`, `stock`, `photo`) VALUES
(1, 'Core Racerback Tank', 'nike', 'medium', 'electric blue', 'women', 29.99, 150, '<FileStorage: \'Core Racerback Tank.jpg\' (\'image/jpeg\')>'),
(2, 'Core Racerback Tank', 'nike', 'medium', 'electric blue', 'women', 29.99, 150, 'Core Racerback Tank.jpg'),
(3, 'Core Racerback Tank', 'nike', 'medium', 'electric blue', 'women', 29.99, 150, 'Core Racerback Tank.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `employees`
--

CREATE TABLE `employees` (
  `emp_id` int(11) NOT NULL,
  `emp_name` varchar(100) DEFAULT NULL,
  `hire_date` date DEFAULT NULL,
  `dept_id` int(11) DEFAULT NULL,
  `salary` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employees`
--

INSERT INTO `employees` (`emp_id`, `emp_name`, `hire_date`, `dept_id`, `salary`) VALUES
(2, 'Josephine', '2024-02-01', 1, 95000.00),
(3, 'Jessica', '2023-05-18', 2, 88000.00),
(4, 'Robert', '2023-10-01', 1, 85000.00),
(5, 'Nancy', '2023-03-22', 2, 77000.00),
(6, 'mutua', '2017-01-01', 2, 75000.00),
(7, 'Sarah', '2023-08-05', 1, 85000.00),
(8, 'Michael', '2023-02-15', 2, 61000.00),
(9, 'Linda', '2023-12-20', 3, 95000.00),
(10, 'David', '2023-07-14', 1, 85000.00),
(11, 'Karen', '2024-03-01', 2, 91000.00),
(12, 'Charles', '2023-01-10', 3, 69000.00),
(13, 'Mary', '2023-06-30', 2, 72000.00),
(14, 'Joseph', '2023-04-12', 1, 85000.00),
(15, 'Patricia', '2023-09-12', 3, 85000.00),
(16, 'Richard', '2024-02-14', 1, 85000.00),
(17, 'Susan', '2023-05-01', 2, 81000.00),
(18, 'Thomas', '2023-11-05', 3, 56000.00),
(19, 'Christopher', '2023-08-25', 1, 85000.00),
(20, 'James', '2017-01-01', 2, 75000.00),
(21, 'Elizabeth', '2023-03-05', 1, 85000.00),
(22, 'Daniel', '2024-01-05', 3, 64000.00),
(23, 'Matthew', '2023-12-01', 2, 57000.00);

-- --------------------------------------------------------

--
-- Table structure for table `fitnesssupplements`
--

CREATE TABLE `fitnesssupplements` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `brand` varchar(100) NOT NULL,
  `dosage` varchar(50) NOT NULL,
  `expiry` date NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `stock` int(11) NOT NULL,
  `photo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `fitnesssupplements`
--

INSERT INTO `fitnesssupplements` (`id`, `name`, `brand`, `dosage`, `expiry`, `price`, `stock`, `photo`) VALUES
(1, 'Pure Creatine Monohydrate', 'USN (Ultimate Sports Nutrition)', '5g per serving (1 scoop)', '2026-04-30', 1.00, 50, '<FileStorage: \'Pure Creatine Monohydrate.jpg\' (\'image/jpeg\')>'),
(2, 'Pure Creatine Monohydrate', 'USN (Ultimate Sports Nutrition)', '5g per serving (1 scoop)', '2026-04-30', 1.00, 50, 'Pure Creatine Monohydrate.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `active_wear`
--
ALTER TABLE `active_wear`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `employees`
--
ALTER TABLE `employees`
  ADD PRIMARY KEY (`emp_id`);

--
-- Indexes for table `fitnesssupplements`
--
ALTER TABLE `fitnesssupplements`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `active_wear`
--
ALTER TABLE `active_wear`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `fitnesssupplements`
--
ALTER TABLE `fitnesssupplements`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
