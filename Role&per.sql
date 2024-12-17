CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,  -- Hashed Password
    role VARCHAR(20) NOT NULL        -- e.g., 'admin', 'manager', 'viewer'
);

CREATE TABLE permissions (
    role VARCHAR(20) PRIMARY KEY,
    can_view BOOLEAN DEFAULT FALSE,
    can_edit BOOLEAN DEFAULT FALSE,
    can_delete BOOLEAN DEFAULT FALSE
);

-- Insert role permissions
INSERT INTO permissions (role, can_view, can_edit, can_delete) VALUES ('admin', TRUE, TRUE, TRUE);
INSERT INTO permissions (role, can_view, can_edit, can_delete) VALUES ('manager', TRUE, TRUE, FALSE);
INSERT INTO permissions (role, can_view, can_edit, can_delete) VALUES ('viewer', TRUE, FALSE, FALSE);
