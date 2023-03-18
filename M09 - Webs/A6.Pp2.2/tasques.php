<?php
/*
Plugin Name: Task List
Description: A plugin to display and manage project tasks
Version: 1.0
Author: Nil Massó
*/

function task_list_shortcode() {
    global $wpdb;
    
    // Check for task deletions
    if (isset($_POST['task'])) {
        $wpdb->delete($wpdb->prefix . 'tasks', array('task' => $_POST['task']));
    }
    
    // Get remaining tasks
    $tasks = $wpdb->get_results("SELECT task FROM " . $wpdb->prefix . "tasks");
    
    // Display task list
    $output = '<h2>Task List</h2>';
    $output .= '<ul>';
    foreach ($tasks as $task) {
        $output .= '<li>' . $task->task . ' <form method="post"><input type="hidden" name="task" value="' . $task->task . '"><input type="submit" value="Delete"></form></li>';
    }
    $output .= '</ul>';
    
    return $output;
}
add_shortcode('task-list', 'task_list_shortcode');

// Create tasks table on plugin activation
function task_list_activate() {
    global $wpdb;
    
    $table_name = $wpdb->prefix . 'tasks';
    
    $charset_collate = $wpdb->get_charset_collate();
    
    $sql = "CREATE TABLE if not exists $table_name (
        id mediumint(9) NOT NULL AUTO_INCREMENT,
        task text NOT NULL,
        end_date date DEFAULT '0000-00-00' NOT NULL,
        PRIMARY KEY (id)
    ) $charset_collate;";
    
    require_once(ABSPATH . 'wp-admin/includes/upgrade.php');
    dbDelta($sql);

    // Add initial tasks to database if table is empty
    if ($wpdb->get_var("SELECT COUNT(*) FROM " . $wpdb->prefix . "tasks") == 0) {
        $wpdb->insert($wpdb->prefix . 'tasks', array('task' => 'Crear la base de dades', 'end_date' => '2023-12-01'));
        $wpdb->insert($wpdb->prefix . 'tasks', array('task' => 'Crear el plugin', 'end_date' => '2023-12-02'));
        $wpdb->insert($wpdb->prefix . 'tasks', array('task' => 'Crear la web', 'end_date' => '2023-12-03'));
    }
}
register_activation_hook(__FILE__, 'task_list_activate');
?>