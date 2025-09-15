-- Xóa các bảng nếu chúng đã tồn tại để tránh lỗi khi chạy lại script
DROP TABLE IF EXISTS `notes`;
DROP TABLE IF EXISTS `users`;

-- =============================================
-- Bảng USERS: Lưu thông tin người dùng
-- =============================================
CREATE TABLE `users` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(100) NOT NULL COMMENT 'Tên đầy đủ của người dùng',
    `username` VARCHAR(50) NOT NULL UNIQUE COMMENT 'Tên đăng nhập, không trùng lặp',
    `password` VARCHAR(255) NOT NULL COMMENT 'Nên lưu mật khẩu đã được băm (hashed)',
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) COMMENT='Lưu trữ thông tin người dùng';


-- =============================================
-- Bảng NOTES: Lưu các ghi chú của người dùng
-- =============================================
CREATE TABLE `notes` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `content` TEXT NOT NULL COMMENT 'Nội dung của ghi chú',
    `user_id` INT NOT NULL,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Thiết lập khóa ngoại liên kết đến bảng users
    -- ON DELETE CASCADE: Nếu một user bị xóa, tất cả ghi chú của họ cũng sẽ bị xóa
    FOREIGN KEY (`user_id`) REFERENCES `users`(`id`) ON DELETE CASCADE
) COMMENT='Lưu trữ các ghi chú do người dùng tạo';


-- =============================================
-- CHÈN DỮ LIỆU MẪU (TÙY CHỌN)
-- =============================================
-- Thêm 2 người dùng mẫu
INSERT INTO `users` (`name`, `username`, `password`) VALUES 
('Văn An', 'vanan', 'hashed_password_1'),
('Thị Bình', 'thibinh', 'hashed_password_2');

-- Thêm 3 ghi chú mẫu, liên kết với 2 người dùng trên
-- user_id = 1 tương ứng với 'vanan'
-- user_id = 2 tương ứng với 'thibinh'
INSERT INTO `notes` (`content`, `user_id`) VALUES
('Hôm nay trời đẹp.', 1),
('Cần đi siêu thị mua rau củ.', 2),
('Đừng quên gọi điện cho mẹ.', 2);