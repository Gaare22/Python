-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 27, 2022 at 03:29 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_tiket`
--

-- --------------------------------------------------------

--
-- Table structure for table `tb_jadwa`
--

CREATE TABLE `tb_jadwa` (
  `kode_jadwal` varchar(5) NOT NULL,
  `kode_bandara` varchar(5) NOT NULL,
  `jadwal` varchar(10) NOT NULL,
  `pukul` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_jadwa`
--

INSERT INTO `tb_jadwa` (`kode_jadwal`, `kode_bandara`, `jadwal`, `pukul`) VALUES
('M1', 'PLG', 'MALAM', '20:00:00'),
('M10', 'BDG', 'MALAM', '00:30:00'),
('M11', 'SBY', 'MALAM', '01:00:00'),
('M12', 'MDN', 'MALAM', '01:30:00'),
('M13', 'SMG', 'MALAM', '02:00:00'),
('M14', 'PDG', 'MALAM', '02:30:00'),
('M2', 'BDG', 'MALAM', '20:30:00'),
('M3', 'SBY', 'MALAM', '21:00:00'),
('M4', 'MDN', 'MALAM', '21:30:00'),
('M5', 'SMG', 'MALAM', '22:00:00'),
('M6', 'PDG', 'MALAM', '22:30:00'),
('M7', 'BLI', 'MALAM', '23:00:00'),
('M8', 'JKT', 'MALAM', '23:30:00'),
('M9', 'PLG', 'MALAM', '00:00:00'),
('PG1', 'BLI', 'PAGI', '03:00:00'),
('PG10', 'JKT', 'PAGI', '07:30:00'),
('PG11', 'PLG', 'PAGI', '08:00:00'),
('PG12', 'BDG', 'PAGI', '08:30:00'),
('PG13', 'SBY', 'PAGI', '09:00:00'),
('PG14', 'MDN', 'PAGI', '09:30:00'),
('PG15', 'SMG', 'PAGI', '10:00:00'),
('PG16', 'PDG', 'PAGI', '10:30:00'),
('PG17', 'BLI', 'PAGI', '11:00:00'),
('PG18', 'JKT', 'PAGI', '11:30:00'),
('PG2', 'JKT', 'PAGI', '03:30:00'),
('PG3', 'PLG', 'PAGI', '04:00:00'),
('PG4', 'BDG', 'PAGI', '04:30:00'),
('PG5', 'SBY', 'PAGI', '05:00:00'),
('PG6', 'MDN', 'PAGI', '05:30:00'),
('PG7', 'SMG', 'PAGI', '06:00:00'),
('PG8', 'PDG', 'PAGI', '06:30:00'),
('PG9', 'BLI', 'PAGI', '07:00:00'),
('SG1', 'PLG', 'SIANG', '12:00:00'),
('SG2', 'BDG', 'SIANG', '12:30:00'),
('SG3', 'SBY', 'SIANG', '13:00:00'),
('SG4', 'MDN', 'SIANG', '13:30:00'),
('SG5', 'SMG', 'SIANG', '14:00:00'),
('SG6', 'PDG', 'SIANG', '14:30:00'),
('SG7', 'BLI', 'SIANG', '15:00:00'),
('SG8', 'JKT', 'SIANG', '15:30:00'),
('SR1', 'PLG', 'SORE', '16:00:00'),
('SR2', 'BDG', 'SORE', '16:30:00'),
('SR3', 'SBY', 'SORE', '17:00:00'),
('SR4', 'MDN', 'SORE', '17:30:00'),
('SR5', 'SMG', 'SORE', '18:00:00'),
('SR6', 'PDG', 'SORE', '18:30:00'),
('SR7', 'BLI', 'SORE', '19:00:00'),
('SR8', 'JKT', 'SORE', '19:30:00');

-- --------------------------------------------------------

--
-- Table structure for table `tb_kelas`
--

CREATE TABLE `tb_kelas` (
  `kode_kelas` varchar(11) NOT NULL,
  `kode_bandara` varchar(5) NOT NULL,
  `kelas` varchar(20) NOT NULL,
  `harga` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_kelas`
--

INSERT INTO `tb_kelas` (`kode_kelas`, `kode_bandara`, `kelas`, `harga`) VALUES
('BDG1', 'BDG', 'FIRST', 2000000),
('BDG2', 'BDG', 'BISNIS', 1000000),
('BDG3', 'BDG', 'EKONOMI', 500000),
('BLI1', 'BLI', 'FIRST', 6000000),
('BLI2', 'BLI', 'BISNIS', 4000000),
('BLI3', 'BLI', 'EKONOMI', 2000000),
('JKT1', 'JKT', 'FIRST', 2000000),
('JKT2', 'JKT', 'BISNIS', 1000000),
('JKT3', 'JKT', 'EKONOMI', 500000),
('MDN1', 'MDN', 'FIRST', 7000000),
('MDN2', 'MDN', 'BISNIS', 5000000),
('MDN3', 'MDN', 'EKONOMI', 2500000),
('PDG1', 'PDG', 'FIRST', 5000000),
('PDG2', 'PDG', 'BISNIS', 4000000),
('PDG3', 'PDG', 'EKONOMI', 2000000),
('PLG1', 'PLG', 'FIRST', 4000000),
('PLG2', 'PLG', 'BISNIS', 2000000),
('PLG3', 'PLG', 'EKONOMI', 1500000),
('SBY1', 'SBY', 'FIRST', 2000000),
('SBY2', 'SBY', 'BISNIS', 1000000),
('SBY3', 'SBY', 'EKONOMI', 500000),
('SMG1', 'SMG', 'FIRST', 2000000),
('SMG2', 'SMG', 'BISNIS', 1000000),
('SMG3', 'SMG', 'EKONOMI', 500000);

-- --------------------------------------------------------

--
-- Table structure for table `tb_pemesanan`
--

CREATE TABLE `tb_pemesanan` (
  `id_pemesanan` int(11) NOT NULL,
  `kode_pemesanan` varchar(10) NOT NULL,
  `id_user1` varchar(11) NOT NULL,
  `kode_bandara` varchar(5) NOT NULL,
  `kode_jadwal` varchar(5) NOT NULL,
  `kode_kelas` varchar(20) NOT NULL,
  `jenis_kelamin1` varchar(11) NOT NULL,
  `berangkat` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_pemesanan`
--

INSERT INTO `tb_pemesanan` (`id_pemesanan`, `kode_pemesanan`, `id_user1`, `kode_bandara`, `kode_jadwal`, `kode_kelas`, `jenis_kelamin1`, `berangkat`) VALUES
(15, '', 'LKSKD', 'SMG', 'M13', 'SMG1', '', ''),
(18, '11', 'TEGAR RAKAS', 'SBY', 'M3', 'SBY1', 'Laki-laki', '2022/12/21'),
(21, '14', 'TERASI', 'PLG', 'm1', 'PLG1', 'Laki-laki', '2022/12/12'),
(16, '15', 'Tegar', 'SMG', 'M5', 'SMG1', 'Laki-laki', '2022/12/12'),
(19, '17', 'YSHDG', 'BLI', 'M7', 'BLI1', 'Laki-laki', '2022/12/12'),
(17, '3', 'TEGAR RAKAS', 'BLI', 'M7', 'BLI1', 'Laki-laki', '2022/12/31'),
(20, '5', 'TEHG', 'SMG', 'm5', 'Smg3', 'Laki-laki', '2022/12/12');

-- --------------------------------------------------------

--
-- Table structure for table `tb_tiket`
--

CREATE TABLE `tb_tiket` (
  `kode_bandara` varchar(5) NOT NULL,
  `kota_tujuan` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_tiket`
--

INSERT INTO `tb_tiket` (`kode_bandara`, `kota_tujuan`) VALUES
('BDG', 'BANDUNG'),
('BLI', 'BALI'),
('JKT', 'JAKARTA'),
('MDN', 'MEDAN'),
('PDG', 'PADANG'),
('PLG', 'PALEMBANG'),
('SBY', 'SURABAYA'),
('SMG', 'SEMARANG');

-- --------------------------------------------------------

--
-- Table structure for table `tb_user`
--

CREATE TABLE `tb_user` (
  `id_user` int(11) NOT NULL,
  `nama` varchar(30) NOT NULL,
  `jenis_kelamin` varchar(5) NOT NULL,
  `tanggal_keberangkatan` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tb_user`
--

INSERT INTO `tb_user` (`id_user`, `nama`, `jenis_kelamin`, `tanggal_keberangkatan`) VALUES
(135, 'hdjdhjdhaj', 'Laki-', '0000-00-00'),
(136, 'kdsjksjdks', 'Laki-', '0000-00-00'),
(137, 'dadjkdja', 'Laki-', '0000-00-00'),
(138, 'dkkdjkjad', 'Laki-', '0000-00-00'),
(139, 'skdjksjdksjd', 'Laki-', '0000-00-00'),
(140, 'Hjhajshjshja', 'Laki-', '0000-00-00'),
(141, 'LLL', 'Laki-', '0000-00-00'),
(142, 'LLLL', 'Laki-', '0000-00-00'),
(143, 'TEGAR', 'Laki-', '2022-12-31'),
(144, 'TRG', 'Laki-', '0000-00-00'),
(145, 'Jdkdjkd', 'Laki-', '0000-00-00'),
(146, 'LLD', 'Laki-', '0000-00-00'),
(147, 'LLL', 'Laki-', '2022-12-21'),
(148, 'TEGAR', 'Laki-', '2022-12-21'),
(149, 'TEGAR', 'Laki-', '2022-12-12'),
(150, 'LKSKD', 'Laki-', '2022-12-12'),
(151, 'TEGAR', 'Laki-', '2022-12-12'),
(152, 'TEGAR', 'Laki-', '2022-11-11'),
(153, 'TEGAR', 'Laki-', '2022-12-12'),
(154, 'Tegar', 'Laki-', '2022/12/12'),
(155, 'TEGAR RAKASIWI', 'Laki-', '2022/12/31'),
(156, 'TEGAR RAKASIWI', 'Laki-', '2022/12/21'),
(157, 'TEGAR RAKASIWI', 'Laki-', '2022/11/11'),
(158, 'TEGSH', 'Laki-', '2022/12/12'),
(159, 'TEGAR RAKASIWI', 'Laki-', '2022/11/11'),
(160, 'RAKASIWI', 'Laki-', '2022/12/12'),
(161, 'RAKASIWI', 'Laki-', '2022/12/12'),
(162, 'YSHDG', 'Laki-', '2022/12/12'),
(163, 'TEHG', 'Laki-', '2022/12/12'),
(164, 'TERASI', 'Laki-', '2022/12/12'),
(165, 'TERASI', 'Laki-', '2022/12/12');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_jadwa`
--
ALTER TABLE `tb_jadwa`
  ADD PRIMARY KEY (`kode_jadwal`),
  ADD KEY `kode_bandara_FOREIGN2` (`kode_bandara`) USING BTREE;

--
-- Indexes for table `tb_kelas`
--
ALTER TABLE `tb_kelas`
  ADD PRIMARY KEY (`kode_kelas`),
  ADD KEY `kode_bandara_FOREIGN` (`kode_bandara`);

--
-- Indexes for table `tb_pemesanan`
--
ALTER TABLE `tb_pemesanan`
  ADD PRIMARY KEY (`id_pemesanan`),
  ADD KEY `kode_pemesanan` (`kode_pemesanan`,`id_user1`,`kode_bandara`,`kode_jadwal`,`kode_kelas`,`jenis_kelamin1`,`berangkat`),
  ADD KEY `kode_bandara` (`kode_bandara`),
  ADD KEY `kode_kelas` (`kode_kelas`),
  ADD KEY `kode_jadwal_FOREIGN` (`kode_jadwal`) USING BTREE;

--
-- Indexes for table `tb_tiket`
--
ALTER TABLE `tb_tiket`
  ADD PRIMARY KEY (`kode_bandara`);

--
-- Indexes for table `tb_user`
--
ALTER TABLE `tb_user`
  ADD PRIMARY KEY (`id_user`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tb_pemesanan`
--
ALTER TABLE `tb_pemesanan`
  MODIFY `id_pemesanan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `tb_user`
--
ALTER TABLE `tb_user`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=166;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `tb_jadwa`
--
ALTER TABLE `tb_jadwa`
  ADD CONSTRAINT `tb_jadwa_ibfk_1` FOREIGN KEY (`kode_bandara`) REFERENCES `tb_tiket` (`kode_bandara`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tb_kelas`
--
ALTER TABLE `tb_kelas`
  ADD CONSTRAINT `tb_kelas_ibfk_1` FOREIGN KEY (`kode_bandara`) REFERENCES `tb_tiket` (`kode_bandara`);

--
-- Constraints for table `tb_pemesanan`
--
ALTER TABLE `tb_pemesanan`
  ADD CONSTRAINT `tb_pemesanan_ibfk_1` FOREIGN KEY (`kode_bandara`) REFERENCES `tb_tiket` (`kode_bandara`),
  ADD CONSTRAINT `tb_pemesanan_ibfk_2` FOREIGN KEY (`kode_kelas`) REFERENCES `tb_kelas` (`kode_kelas`),
  ADD CONSTRAINT `tb_pemesanan_ibfk_3` FOREIGN KEY (`kode_jadwal`) REFERENCES `tb_jadwa` (`kode_jadwal`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
