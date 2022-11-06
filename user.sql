-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th10 06, 2022 lúc 03:55 PM
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
-- Cấu trúc bảng cho bảng `otp_management`
--

CREATE TABLE `otp_management` (
  `otpId` int(11) NOT NULL,
  `otp` int(11) DEFAULT NULL,
  `token` int(11) DEFAULT NULL,
  `time_send` varchar(64) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `schoolfee`
--

CREATE TABLE `schoolfee` (
  `mssv` int(11) NOT NULL,
  `hoTen` varchar(64) DEFAULT NULL,
  `soTien` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `schoolfee`
--

INSERT INTO `schoolfee` (`mssv`, `hoTen`, `soTien`) VALUES
(52000101, 'Ngoc Linh', 11000000),
(52000102, 'Vy Nhan', 12300000),
(52000103, 'Linh Chi', 42000000),
(52000104, 'Hoang Ngan', 16000000),
(52000105, 'Lam Anh', 14000000),
(52000106, 'Ngoc Nam', 1000000),
(52000107, 'Sieu vy', 22000000),
(52000896, 'Tong Duc Thanh Nam', 11000000);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `transactionhistory`
--

CREATE TABLE `transactionhistory` (
  `transactionHistoryCode` varchar(64) NOT NULL,
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
  `mssv` int(11) DEFAULT NULL,
  `transactionHistoryCode` varchar(64) DEFAULT NULL,
  `transactionTime` varchar(64) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
(51900001, 'user6', '123456', '0123332211', 'pnworkspaceonly@gmail.com', 9000000, 'TH1'),
(51900123, 'user2', '123456', '0398547673', 'pnworkspaceonly@gmail.com', 120000000, 'TH2'),
(51900456, 'user3', '123456', '0398738812', 'pnworkspaceonly@gmail.com', 70000000, 'TH3'),
(51900698, 'user1', '123456', '0398547674', 'pnworkspaceonly@gmail.com', 10000000, 'TH4'),
(51900789, 'user5', '123456', '0322133257', 'pnworkspaceonly@gmail.com', 12000000, 'TH5');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `otp_management`
--
ALTER TABLE `otp_management`
  ADD PRIMARY KEY (`otpId`);

--
-- Chỉ mục cho bảng `schoolfee`
--
ALTER TABLE `schoolfee`
  ADD PRIMARY KEY (`mssv`);

--
-- Chỉ mục cho bảng `transactionhistory`
--
ALTER TABLE `transactionhistory`
  ADD PRIMARY KEY (`transactionHistoryCode`);

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
-- AUTO_INCREMENT cho bảng `otp_management`
--
ALTER TABLE `otp_management`
  MODIFY `otpId` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `schoolfee`
--
ALTER TABLE `schoolfee`
  MODIFY `mssv` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=52000897;

--
-- AUTO_INCREMENT cho bảng `transactionprocessing`
--
ALTER TABLE `transactionprocessing`
  MODIFY `transactionProcessingCode` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT cho bảng `users`
--
ALTER TABLE `users`
  MODIFY `userId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51900790;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
