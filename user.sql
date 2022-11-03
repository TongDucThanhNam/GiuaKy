-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th10 03, 2022 lúc 03:01 PM
-- Phiên bản máy phục vụ: 10.4.25-MariaDB
-- Phiên bản PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `user`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `schoolfee`
--

CREATE TABLE `schoolfee` (
  `mssv` varchar(64) DEFAULT NULL,
  `hoTen` varchar(64) DEFAULT NULL,
  `soTien` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `schoolfee`
--

INSERT INTO `schoolfee` (`mssv`, `hoTen`, `soTien`) VALUES
('52000896', '123', 11000000);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `transactionhistory`
--

CREATE TABLE `transactionhistory` (
  `transactionHistoryCode` varchar(64) DEFAULT NULL,
  `dayTrade` varchar(64) DEFAULT NULL,
  `transactionAmount` int(11) DEFAULT NULL,
  `balanceAfterTransaction` int(11) DEFAULT NULL,
  `content` varchar(64) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `transactionprocessing`
--

CREATE TABLE `transactionprocessing` (
  `transactionProcessingCode` int(11) NOT NULL,
  `userId` int(11) DEFAULT NULL,
  `transactionHistoryCode` varchar(64) DEFAULT NULL,
  `transactionTime` varchar(64) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `transactionprocessing`
--

INSERT INTO `transactionprocessing` (`transactionProcessingCode`, `userId`, `transactionHistoryCode`, `transactionTime`) VALUES
(1, 1, 'TH01', '12/12/2002'),
(2, 1, 'TH01', '19/05/2002'),
(3, 1, 'TH01', '19/05/2002'),
(4, 1, 'TH01', '19/05/2002'),
(5, 1, 'TH01', '19/05/2002'),
(6, 1, 'TH01', '19/05/2002'),
(7, 1, 'TH01', '19/05/2002');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `users`
--

CREATE TABLE `users` (
  `userId` int(11) NOT NULL,
  `userName` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL,
  `phone` varchar(64) DEFAULT NULL,
  `email` varchar(64) DEFAULT NULL,
  `balance` int(11) DEFAULT NULL,
  `tradeHistoryCode` varchar(64) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `users`
--

INSERT INTO `users` (`userId`, `userName`, `password`, `phone`, `email`, `balance`, `tradeHistoryCode`) VALUES
(1, 'admin', 'admin', '0909205124', 'nam@gmail.com', 120000, 'TH01');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `transactionprocessing`
--
ALTER TABLE `transactionprocessing`
  ADD PRIMARY KEY (`transactionProcessingCode`);

--
-- Chỉ mục cho bảng `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`userId`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `transactionprocessing`
--
ALTER TABLE `transactionprocessing`
  MODIFY `transactionProcessingCode` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT cho bảng `users`
--
ALTER TABLE `users`
  MODIFY `userId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
