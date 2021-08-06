-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 06 Agu 2021 pada 23.05
-- Versi server: 10.4.10-MariaDB
-- Versi PHP: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `crud_family_tree`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `families`
--

CREATE TABLE `families` (
  `id` int(11) NOT NULL,
  `nama` varchar(100) DEFAULT NULL,
  `jenis_kelamin` varchar(20) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `child_of` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `families`
--

INSERT INTO `families` (`id`, `nama`, `jenis_kelamin`, `parent_id`, `child_of`) VALUES
(1, 'Budi', 'Pria', 0, NULL),
(3, 'Dedi', 'Pria', 1, 0),
(4, 'Dodi', 'Pria', 2, 0),
(5, 'Dede', 'Pria', 3, 0),
(6, 'Dewi', 'Wanita', 4, 0),
(7, 'Feri', 'Pria', 5, 1),
(8, 'Farah', 'Wanita', 6, 1),
(9, 'Gugus', 'Pria', 7, 2),
(10, 'Gandi', 'Pria', 8, 2),
(11, 'Hani', 'Wanita', 9, 3),
(12, 'Hana', 'Wanita', 10, 3);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `families`
--
ALTER TABLE `families`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `families`
--
ALTER TABLE `families`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
