<script>
    var start_time = 0;
    function updateTime() {
        if (start_time == 0) {
            start_time = ' . time() . ';
        } else {
            start_time = start_time;
        }
        var end_time = ' . time() . ';
        var total_seconds = end_time - start_time;
        var hours = Math.floor(total_seconds / 3600);
        total_seconds %= 3600;
        var minutes = Math.floor(total_seconds / 60);
        var seconds = total_seconds % 60;
        document.getElementById("elapsed-time").innerHTML = hours + "h " + minutes + "m " + seconds + "s";
    }
</script>
<?php
/*
Plugin Name: Hour Counter
Description: A plugin to count hours worked
Version: 1.0
Author: Nil Massó
*/

function hour_counter_shortcode() {
    global $wpdb;
    
    // Get total hours from database
    $total_hours = $wpdb->get_var("SELECT total_hours FROM " . $wpdb->prefix . "hours" . " WHERE id = 1");
    // Check for timer start and stop
    if (isset($_POST['start'])) {
        update_option('hour_counter_start', time());
    } elseif (isset($_POST['stop'])) {
        $start_time = get_option('hour_counter_start');
        if ($start_time) {
            $end_time = time();
            $hours = ($end_time - $start_time) / 3600;
            $total_hours += $hours;
            $wpdb->replace($wpdb->prefix . 'hours', array('total_hours' => $total_hours) + array('id' => 1));
            delete_option('hour_counter_start');
        }
    }    
    
    // Display hour counter
    $output = '<h2>Hour Counter</h2>';
    $output .= '<p>Total hours: ' . number_format($total_hours, 2) . '</p>';
    //Elapsed time in real time using JavaScript
    $output .= '<p>Elapsed time: <span id="elapsed-time">0</span> seconds</p>';
    $output .= '<form method="post">';
    if (get_option('hour_counter_start')) {
        $output .= '<input type="submit" name="stop" value="Stop">';
    } else {
        $output .= '<input type="submit" name="start" value="Start" onclick="setInterval(updateTime, 1000)">';
    }
    $output .= '</form>';

    return $output;
}
add_shortcode('hour-counter', 'hour_counter_shortcode');

// Create hours table on plugin activation
function hour_counter_activate() {
    global $wpdb;
    
    $table_name = $wpdb->prefix . 'hours';
    
    $charset_collate = $wpdb->get_charset_collate();
    
    $sql = "CREATE TABLE if not exists $table_name (
        id mediumint(9) NOT NULL AUTO_INCREMENT,
        total_hours float(10) NOT NULL,
        PRIMARY KEY (id)
    ) $charset_collate;";
    
    require_once(ABSPATH . 'wp-admin/includes/upgrade.php');
    dbDelta($sql);
    
    $wpdb->insert($table_name, array('total_hours' => 0));
}
register_activation_hook(__FILE__, 'hour_counter_activate');

?>