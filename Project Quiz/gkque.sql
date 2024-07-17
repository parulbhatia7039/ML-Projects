-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 07, 2023 at 10:06 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `project_quiz`
--

-- --------------------------------------------------------

--
-- Table structure for table `gkque`
--

CREATE TABLE `gkque` (
  `Qnum` int(225) NOT NULL,
  `Ques` varchar(225) NOT NULL,
  `Op1` varchar(225) NOT NULL,
  `Op2` varchar(225) NOT NULL,
  `Op3` varchar(225) NOT NULL,
  `Op4` varchar(225) NOT NULL,
  `CorrectOp` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `gkque`
--

INSERT INTO `gkque` (`Qnum`, `Ques`, `Op1`, `Op2`, `Op3`, `Op4`, `CorrectOp`) VALUES
(1, 'Blue Ocean, the World’s most powerful Supercomputer, is specifically designed for:', 'NASA', 'US Naval Oceanographic office', 'US Federal Reserve Bank', 'US Intelligence Agency', 'B'),
(2, 'India’s first Jan Shatabdi Express between Mumbai-Goa was commenced on:', 'April 16, 2002', 'April 20, 2002', 'June 20, 2002', 'June 16, 2002', 'A'),
(3, '1st developing country in the world to make use of fire optics technology is:', 'China', 'Japan', 'India', 'Vietnam', 'C'),
(4, 'Which state possesses the maximum percentage of SC population?', 'U.P.', 'M.P.', 'Kerala', 'Punjab', 'D'),
(5, 'Which of the following rivers passes through Himachal Pradesh?    ', 'Chenab', 'Ravi', 'Jhelum', 'Sutlej', 'A'),
(6, 'What is the pH value of the human body?', '9.2 to 9.8', '7.0 to 7.8', '6.1 to 6.3', '5.4 to 5.6', 'B'),
(7, 'Which of the given cities is located on the bank of river Ganga?', 'Patna', 'Gwalior', 'Bhopal', 'Mathura', 'A'),
(8, 'Which of the given devices is used for counting blood cells?', 'Hmelethometer', 'Spyscometer', 'Hemocytometer', 'Hamosytometer', 'C'),
(9, 'Digestion of food in human beings begins in which part of the alimentary canal?', 'Liver', 'Kidney', 'Mouth', 'Large intestine', 'C'),
(10, 'Salt is obtained from sea water through which process.', 'Adsorption', 'Evaporation', 'Sublimation', 'Absorption', 'B'),
(11, 'The hottest planet in the solar system?', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'B'),
(12, 'Who among the following created the Khalsa Panth?', 'Guru Teg Bahadur', 'Guru Hargobind', 'Guru Gobind Singh', 'Guru Arjan Dev', 'C'),
(13, 'Which state is known as the ‘Spice Garden of India’?', 'Kerala', 'Karnataka', 'Andhra Pradesh', 'Tamil Nadu', 'A'),
(14, 'Where was the electricity supply first introduced in India –', 'Mumbai', 'Dehradun', 'Darjeeling', 'Chennai', 'C'),
(15, 'Apart from Venus, which planet rotates from east to west?', 'Jupiter', 'Mars', 'Uranus', 'Earth', 'C'),
(16, 'Which of the three banks will be merged with the other two to create India’s third-largest bank?', 'Punjab National Bank', 'Indian Bank', 'Bank of Baroda', 'Dena Bank', 'B'),
(17, 'Where was India’s first national Museum opened?', 'Delhi', 'Hyderabad', 'Rajasthan', 'Mumbai', 'D'),
(18, 'The world’s nation 5G mobile network was launched by which country?', 'Japan', 'Asia', 'South Korea', 'Malaysia     ', 'C'),
(19, 'The green planet in the solar system is?', 'Mars', 'Uranus', 'Venus', 'Earth       ', 'B'),
(20, 'The father of Indian missile technology is _________________?', 'Dr Homi Bhabha', 'Dr Chidambaram', 'Dr U.R. Rao', 'Dr A.P.J. Abdul Kalam      ', 'D'),
(21, 'What is the reason behind the Bats flying in the dark?', 'They produce Ultrasonics', 'The light startles them', 'They have a perfect vision in the dark', 'None of the above    ', 'A'),
(22, 'The study of Heavenly bodies is Known as _________?', 'Astrophysics', 'Astronautics', 'Astrology', 'Astronomy      ', 'D'),
(23, 'Which of the following monuments is not in Delhi?', 'Purana Kila', 'Qutab Minaar', 'Red Fort', 'Char Minaar', 'D'),
(24, 'Which is the part of the computer system that one can physically touch?', 'Data', 'Operating systems', 'Hardware', 'Software', 'C'),
(25, 'Which of the following is NOT a computer programming language?', 'PHP', 'C++', 'Java', 'Microsoft', 'D'),
(26, 'What is the intersection of a column and a row on a worksheet called?', 'Column', 'Value', 'Address', 'Cell', 'D'),
(27, '‘IC’ chips of computers are usually made of...', 'Lead', 'Chromium', 'Silicon', 'Platinum   ', 'C'),
(28, 'Which country has the largest population?', 'U.S.A.', 'U.S.S.R.', 'China', 'India  ', 'C'),
(29, 'Recently NASA launched LRO and LCROSS for the purpose of exploration of...', 'Venus', 'Moon', 'Saturn', 'Jupiter', 'B'),
(30, 'world milk production, India ranks...', 'First', 'Second', 'Third', 'Fourth', 'A'),
(31, 'Which of the following countries has approved world’s first dengue vaccine?', 'United Kingdom', 'Canada', 'Mexico', 'France', 'C'),
(32, 'What is the name of the first Indian woman who wins the Man Booker Prize?	', 'Salman Rushdie', 'Arundhati Roy', 'V.S. Naipaul', 'Kiran Desai', 'B'),
(33, 'Why is the colour of papaya yellow?', 'Lycopene', 'Papain', 'Carotene', 'Caricaxanthin', 'D'),
(34, 'In 2017, Who was appointed as the new Brand Ambassador for Swachh Bharat Mission?', 'Kangana Ranaut', 'Priyanka Chopra', 'Anushka Sharma', 'Shilpa Shetty', 'D'),
(35, 'At which place on earth are there days & nights of equal length always?', 'Equator', 'Poles', 'Prime Meridian', 'Nowhere', 'A'),
(36, 'The largest public sector undertaking in the country is?', 'Railways', 'Airways', 'Roadways', 'Iron and Steel Plants', 'A'),
(37, 'The tomb of a Sufi Saint is known as...', 'Idgah', 'Masjid', 'Dargah', 'None of these', 'C'),
(38, 'Which of the given vitamins is responsible for blood clotting?', 'Vitamin A', 'Vitamin B', 'Vitamin K', 'Vitamin D', 'C'),
(39, 'The percentage of white population in South Africa is...', '19%', '25%', '40%', '70%', 'A'),
(40, 'What is the reason behind the Bats flying in the dark?', 'They produce high pitched sounds called ultrasonics', 'The light startles them', 'They have a perfect vision in the dark', 'None of the above', 'A'),
(41, 'Women Helpline Scheme was launched in...', '2012', '2015', '2017', '2018', 'B'),
(42, 'Executables might be called ________', 'native code', 'executable code', 'complex code', 'machine code', 'A'),
(43, 'Who was the first ever Miss Universe from India?', 'Rita Faria', 'Sushmita Sen', 'Lara Dutta', 'Yukta Mookhi', 'B'),
(44, 'The first e-passport in india was issued to...', 'Somnath Chatterjee', 'Pranav Mukherjee', 'Pratibha Patil', 'Narendra Modi', 'C'),
(45, 'Which of the following scheme provide education to girls and their welfare?', 'One Stop Centre Scheme', 'UJJAWALA', 'SWADHAR Scheme', 'Beti Bachao Beti Padhao', 'D'),
(46, 'JIT stands for?', 'Just in time', 'Jump in time', 'Jump in text', 'Jump in terms', 'A'),
(47, 'Which one is the highest Island of world.', 'Borneo', 'Finland', 'Sumatra', 'Greenland', 'D'),
(48, 'Which country of also known as “Land of Rising Sun”.', 'Japan', 'New Zealand', 'Fiji', 'China', 'A'),
(49, 'What animal has the worst memory? ', 'Dog', 'Rat', 'Elephant', 'Dolphin', 'C'),
(50, 'The language made up of binary coded instructions.', 'Machine', 'C Language', 'BASIC', 'High level', 'A');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `gkque`
--
ALTER TABLE `gkque`
  ADD PRIMARY KEY (`Qnum`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `gkque`
--
ALTER TABLE `gkque`
  MODIFY `Qnum` int(225) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
