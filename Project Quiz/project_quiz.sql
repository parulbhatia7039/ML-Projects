-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 03, 2023 at 05:54 AM
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
-- Table structure for table `m_questions`
--

CREATE TABLE `m_questions` (
  `QN` int(255) NOT NULL,
  `Question` varchar(255) NOT NULL,
  `O1` varchar(255) NOT NULL,
  `O2` varchar(255) NOT NULL,
  `O3` varchar(255) NOT NULL,
  `O4` varchar(255) NOT NULL,
  `CO` varchar(255) NOT NULL,
  `CO1` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `m_questions`
--

INSERT INTO `m_questions` (`QN`, `Question`, `O1`, `O2`, `O3`, `O4`, `CO`, `CO1`) VALUES
(1, 'What is the value of (x-a)(x-b)(x-c)........(x-z)=?', '0', 'x', 'x*x', '2x', '0', 'A'),
(2, 'How many vertices are present on a cube?', '6', '8', '10', '12', '8', 'B'),
(3, 'What 3 numbers result in the same answer when they are added or multiplied altogether?', '1,2,3', '1,1,1', '2,2,2', '1,2,1', '1,2,3', 'A'),
(4, 'What is 7% equal to? ', '0.007', '0.07', '0.7', '7', '0.07', 'B'),
(5, 'In a century how many months are there?', '12', '120', '1200', '12000', '1200', 'C'),
(6, 'All natural numbers and 0 are called the ……………… numbers. ', 'whole', 'prime', 'integer', 'rational', 'whole', 'A'),
(7, 'What are the dimensions of the rectangle whose width is 2/3 its length and perimeter is 180m? ', 'Length=36m and Width=54m ', 'Length=24m and Width=16m ', 'Length=54m and Width=36m ', 'Length=18m and Width=12  ', 'Length=24m and Width=16m', 'B'),
(8, 'A typist who can type 50 wpm will take how long to type a 300,000 word book? ', '10 hrs', '60 hrs', '100 hrs', '30 hrs', '100 hrs', 'C'),
(9, 'If 2 sides of a triangle are equal, and one angle is 90 degrees, what are the other 2 angles? ', '90 deg', '45 deg', '30 deg', '60 deg', '45 deg', 'B'),
(10, 'What is the distance between the top of a 30 ft high tower and the tip of its 40 ft long shadow? ', '50 ft', '25 ft', '60 ft', '70 ft', '50 ft', 'A'),
(11, 'What is the number if 10 added to 4 times a number equals 5 less than five times the number? ', '67', '45', '130', '15', '15', 'D'),
(12, 'What are the numbers which are in the ratio of 5:8 and whose sum is 182? ', '70 and 112', '25 and 40', '50 and 80', '40 and 64', '70 and 112', 'A'),
(13, 'What is the square root of 8 x 32? ', '256', '16', '14', '8', '8', 'D'),
(14, 'If 1=3, 2=3, 3=5, 4=4; 5=4, then 6=? ', '2', '5', '3', '4', '3', 'C'),
(15, 'Joey had 6 siblings. All of them were born 2 years apart. The youngest is Chloe who is only 7 years old while Joey is the eldest. Calculate Joey’s age. ', '12', '18', '22', '19', '19', 'D'),
(16, 'Looking at this series: 22, 21, 23, 22, 24, 23, … What number should come next? ', '24', '25', '26', '27', '25', 'B'),
(17, '9876, 6987, 7698, What is the next number in the series?', '8769', '8679', '7689', '9786', '8769', 'A'),
(18, 'There are ten fishes in a tank,two of them drown, four swim away, and three fishes die. What is the number of fish present in the tank?  ', '1', '3', '7', '10', '10', 'D'),
(19, 'When I was four years old, my sister was half my age. Now, I am 18. How old is my sister now?  ', '12', '16', '20', '18', '16', 'B'),
(20, 'Name a triangle whose two angles are equal ', 'Isosceles triangle ', 'Scalene triangle ', 'Right angled triangle', 'None of these', 'Isosceles triangle ', 'A'),
(21, 'What is 20 years called? ', 'Vicennial ', 'Millennium ', 'Decade ', 'Centennial  ', 'Vicennial', 'A'),
(22, 'How many edges does a cylinder have? ', '4', '2', '6', '8', '2', 'B'),
(23, 'How many faces does a square pyramid have? ', '4', '3', '5', '6', '5', 'C'),
(24, 'Find the missing number in the series; 4, 6, 12, 14, 28, 30, (?) ', '38', '44', '32', '60', '60', 'D'),
(25, '', 'The mean, median, and mode are all equal ', 'Only the mean and mode are equal ', ' Only the mean and median are equal ', 'Only the median and mode are equal  ', 'The mean, median, and mode are all equal', ''),
(26, 'The average age of A, B and C was 25 years and that of B and C was 25 years. A’s present age is: ', '30 years', '25 years', '40 years', '42 years', '25 years', 'B'),
(27, 'The average of 5 terms is 50. If the first 4 terms are 45, 42, 119, and 84, what will be the last term? ', '56', '-20', '-40', '-50', '-40', 'C'),
(28, 'The last digit of the number obtained by multiplying the numbers 81 x 52  x  53 x  84  x 55  x 86 x 87 x 85 x 89 will be ', '0', '7', '9', '2', '0', 'A'),
(29, 'The value of tan 4°. tan 43°. tan 47°. tan 86° is  ', '1', '0', '3', '2', '1', 'A'),
(30, 'A kite is flying at a height of 50 metre. If the length of string is 100 metre then the inclination of string to the horizontal ground in degree measure is ', '90', '60', '45', '30', '30', 'D'),
(31, 'A lawn is in the form of a rectangle having its breadth and length respectively in the ratio 2 : 3. The area of the lawn fs 600 sq. metres. Flnd the length of the lawn ', '20m', '30m', '25m', 'None of these', '30m', 'B'),
(32, 'Seven equal cubes each of side 5 cm are joined end to end. Find the surface area of the resulting cuboid. ', '1500 cm2', '750 cm2', '2250 cm2', '700 cm2', '750 cm2', 'B'),
(33, 'If p% of p is 36, then p is equal to : ', '3600', '600', '60', '15', '60', 'C'),
(34, 'If 125% of x is 100, then x is : ', '80', '150', '400', '125', '80', 'A'),
(35, 'What is the name given to a polygon where all the sides and angles are equal? ', 'Equilateral polygon ', 'Equal sided polygon ', 'Regular polygon ', 'Equal polygon  ', 'Regular polygon', 'C'),
(36, 'How many lines of symmetry does an equilateral triangle have? ', 'None', 'Three', 'Four', 'Infinite', 'Three', 'B'),
(37, 'How many lines of symmetry does a circle have? ', 'None', 'Three', 'Four', 'Infinite', 'Infinite', 'D'),
(38, 'Who is the Father of Mathematics?', 'Aryabhatta', 'Ramanujan', 'Archimedes', 'None of these', 'Archimedes', 'C'),
(39, 'When is Pi Day celebrated around the world?', '14 april', '28 january', '14 march', '16 september', '14 march', 'C'),
(40, 'What is the value of cos 360°?', '0', '1', '2', '3', '1', 'B'),
(41, 'Angle greater than 180 degrees but less than 360 degrees are called?', 'Supplementry angles', 'Complementry angles', 'Reflex angles', 'None of these', 'Reflex angles', 'C'),
(42, 'Scientist who was born on Pi Day?', 'Archimedes', 'Albert Einstein', 'Ramanujan', 'Robert Frost', 'Albert Einstein', 'B'),
(43, 'Who invented the equals sign (=) ?', 'Aryabhatta', 'Robert Recorde', 'Ramanujan', 'None of these', 'Robert Recorde', 'B'),
(44, 'Where was Abacus invented?', 'Japan', 'Korea', 'China', 'India', 'China', 'C'),
(45, 'Who is the father of Trigonometry?', 'Robert Hypotenuse', 'Hipparchus', 'Thomas Edison', 'None of these', 'Hipparchus', 'B'),
(46, 'Write the next number of the following Sequences 1,1, 2, 3, 5, 8, 13,_?', '18', '20', '21', '23', '21', 'C'),
(47, 'What do we call people who have a “Fear of Numbers” ?', 'Numberphobia', 'Alphaphobia', 'Numerophobia', 'None of these', 'Numerophobia', 'C'),
(48, 'What is the other name of Multiplication Sign “X” ?', 'Cross sign', 'Number sign', 'Times Sign', 'Inverse division sign', 'Times Sign', 'C'),
(49, 'Which number is Known as Ramanujan-Hardy Number?', '1889', '1649', '1729', '2000', '1729', 'C'),
(50, 'Which number does noy have it\'s reciprocal?', 'Zero', 'One', 'Two', 'Three', 'Zero', 'A'),
(51, 'Which is the smallest Perfect Number?', '4', '9', '16', '6', '6', 'D'),
(52, 'Roman Number of 100 is?', 'C', 'XV', 'XX', 'L', 'C', 'A'),
(53, 'Roman Number of 50?', 'C', 'L', 'XXXXX', 'XV', 'L', 'B');

-- --------------------------------------------------------

--
-- Table structure for table `signup`
--

CREATE TABLE `signup` (
  `S.No` int(255) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Age` int(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Phone Number` varchar(255) NOT NULL,
  `Username` varchar(255) NOT NULL,
  `Password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `signup`
--

INSERT INTO `signup` (`S.No`, `Name`, `Age`, `Email`, `Phone Number`, `Username`, `Password`) VALUES
(4, 'Parul Bhatia', 20, 'bhatiaparul786@gmail.com', '9871260147', 'parul7039', 'Parul@124'),
(5, 'Pppp', 9, 'ppp', '99', 'pp', 'pp');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `m_questions`
--
ALTER TABLE `m_questions`
  ADD PRIMARY KEY (`QN`);

--
-- Indexes for table `signup`
--
ALTER TABLE `signup`
  ADD PRIMARY KEY (`S.No`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `m_questions`
--
ALTER TABLE `m_questions`
  MODIFY `QN` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;

--
-- AUTO_INCREMENT for table `signup`
--
ALTER TABLE `signup`
  MODIFY `S.No` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
