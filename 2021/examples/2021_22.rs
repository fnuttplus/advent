use macroquad::prelude::*;
// use glam::vec3;
use macroquad::models::{Vertex, Mesh};

const MOVE_SPEED: f32 = 0.2;
const LOOK_SPEED: f32 = 0.2;

fn conf() -> Conf {
    Conf {
        window_title: String::from("Macroquad"),
        window_width: 1260,
        window_height: 768,
        fullscreen: false,
        ..Default::default()
    }
}

fn create_mesh(
    x: f32,
    y: f32,
    z: f32,
    w: f32,
    h: f32,
    l: f32,
) -> Mesh {
    Mesh {
        vertices: vec![
            Vertex { // #0
                position: vec3(x, y, h),
                uv: vec2(0.0, 0.0),
                color: WHITE,
            },
            Vertex { // #1
                position: vec3(l, y, h),
                uv: vec2(0.0, 0.0),
                color: WHITE,
            },
            Vertex { // #2
                position: vec3(l, y, z),
                uv: vec2(0.0, 0.0),
                color: WHITE,
            },
            Vertex { // #3
                position: vec3(x, y, z),
                uv: vec2(0.0, 0.0),
                color: WHITE,
            },
            Vertex { // #4
                position: vec3(x, w, h),
                uv: vec2(0.0, 0.0),
                color: WHITE,
            },
            Vertex { // #5
                position: vec3(l, w, h),
                uv: vec2(0.0, 0.0),
                color: WHITE,
            },
            Vertex { // #6
                position: vec3(l, w, z),
                uv: vec2(0.0, 0.0),
                color: WHITE,
            },
            Vertex { // #7
                position: vec3(x, w, z),
                uv: vec2(0.0, 0.0),
                color: WHITE,
            },
        ],
        indices: vec![
            0,1,2,
            0,2,3,
            2,3,6,
            3,6,7,
            4,5,6,
            4,6,7,
            0,1,4,
            1,4,5,
            0,3,4,
            3,4,7,
            1,2,5,
            2,5,6,
        ],
        texture: None,
    }
}


#[macroquad::main(conf)]
async fn main() {
    let world_up = vec3(0.0, 1.0, 0.0);
    let mut yaw: f32 = -0.35;
    let mut pitch: f32 = -0.53;

    let mut front = vec3(
        yaw.cos() * pitch.cos(),
        pitch.sin(),
        yaw.sin() * pitch.cos(),
    )
    .normalize();
    let mut right = front.cross(world_up).normalize();
    let mut up;

    let mut position = vec3(-118.0, 69.0, 29.0);
    let mut last_mouse_position: Vec2 = mouse_position().into();

    let mut grabbed = true;
    set_cursor_grab(grabbed);
    show_mouse(false);

    let background = Color::new(0.059, 0.059, 0.137, 1.0);

    let meshes = vec![
        create_mesh(-32.0, -22.0, -49.0, -29.0, -43.0, 4.0),  
        create_mesh(-22.0, -15.0, -49.0, -46.0, -43.0, 4.0),  
        create_mesh(-22.0, -15.0, -46.0, -29.0, -43.0, -12.0),
        create_mesh(-32.0, -22.0, -29.0, -20.0, -1.0, 4.0),   
        create_mesh(-15.0, 19.0, -49.0, -46.0, -43.0, 4.0),   
        create_mesh(-15.0, 19.0, -46.0, -41.0, -43.0, -12.0), 
        create_mesh(-15.0, 19.0, -41.0, -31.0, -43.0, -35.0), 
        create_mesh(9.0, 19.0, -31.0, -30.0, -43.0, -35.0),   
        create_mesh(9.0, 19.0, -30.0, -29.0, -43.0, -42.0),   
        create_mesh(-15.0, -14.0, -31.0, -29.0, -43.0, -35.0),
        create_mesh(-14.0, 3.0, -31.0, -30.0, -43.0, -35.0),  
        create_mesh(-14.0, 3.0, -30.0, -29.0, -43.0, -42.0),  
        create_mesh(3.0, 9.0, -31.0, -30.0, -43.0, -35.0),    
        create_mesh(3.0, 9.0, -30.0, -29.0, -43.0, -42.0),    
        create_mesh(34.0, 36.0, -31.0, -30.0, -9.0, -8.0),
        create_mesh(34.0, 36.0, -31.0, -30.0, 37.0, 44.0),
        create_mesh(32.0, 34.0, -31.0, -30.0, -9.0, -8.0),
        create_mesh(32.0, 34.0, -31.0, -30.0, 41.0, 44.0),
        create_mesh(34.0, 36.0, -30.0, -29.0, 37.0, 44.0),
        create_mesh(32.0, 34.0, -30.0, -29.0, 41.0, 44.0),
        create_mesh(34.0, 36.0, 16.0, 17.0, 10.0, 44.0),
        create_mesh(32.0, 34.0, 16.0, 17.0, 41.0, 44.0),
        create_mesh(34.0, 36.0, 10.0, 16.0, 10.0, 44.0),
        create_mesh(34.0, 36.0, -29.0, 10.0, 37.0, 44.0),
        create_mesh(32.0, 34.0, -29.0, 16.0, 41.0, 44.0),
        create_mesh(26.0, 32.0, 16.0, 17.0, 41.0, 44.0),
        create_mesh(24.0, 26.0, 16.0, 17.0, 41.0, 44.0),
        create_mesh(24.0, 32.0, 10.0, 16.0, 41.0, 44.0),
        create_mesh(28.0, 32.0, -31.0, 10.0, 41.0, 44.0),
        create_mesh(24.0, 28.0, -1.0, 10.0, 41.0, 44.0),
        create_mesh(24.0, 28.0, -31.0, -1.0, 41.0, 44.0),
        create_mesh(22.0, 24.0, -1.0, 2.0, 41.0, 44.0),
        create_mesh(22.0, 24.0, -31.0, -1.0, 41.0, 44.0),
        create_mesh(18.0, 22.0, -1.0, 0.0, 41.0, 44.0),
        create_mesh(18.0, 22.0, -31.0, -1.0, 41.0, 44.0),
        create_mesh(9.0, 18.0, -31.0, -11.0, 41.0, 44.0),
        create_mesh(18.0, 22.0, 0.0, 2.0, 41.0, 44.0),
        create_mesh(-15.0, -14.0, -31.0, -18.0, 38.0, 44.0),
        create_mesh(-14.0, 9.0, -31.0, -18.0, 41.0, 44.0),
        create_mesh(-15.0, -14.0, -1.0, 0.0, 32.0, 44.0),
        create_mesh(-14.0, 0.0, -1.0, 0.0, 41.0, 44.0),
        create_mesh(-15.0, -14.0, -18.0, -1.0, 38.0, 44.0),
        create_mesh(-14.0, 0.0, -18.0, -1.0, 41.0, 44.0),
        create_mesh(0.0, 9.0, -18.0, -11.0, 41.0, 44.0),
        create_mesh(-15.0, -14.0, 0.0, 2.0, 32.0, 44.0),
        create_mesh(-14.0, 0.0, 0.0, 2.0, 41.0, 44.0),
        create_mesh(22.0, 24.0, 10.0, 17.0, 41.0, 44.0),
        create_mesh(9.0, 22.0, 10.0, 17.0, 41.0, 44.0),
        create_mesh(22.0, 24.0, 2.0, 10.0, 41.0, 44.0),
        create_mesh(18.0, 22.0, 2.0, 10.0, 41.0, 44.0),
        create_mesh(9.0, 18.0, 9.0, 10.0, 41.0, 44.0),
        create_mesh(-14.0, 9.0, 10.0, 17.0, 41.0, 44.0),
        create_mesh(-15.0, -14.0, 2.0, 8.0, 32.0, 44.0),
        create_mesh(-14.0, 0.0, 2.0, 10.0, 41.0, 44.0),
        create_mesh(0.0, 9.0, 9.0, 10.0, 41.0, 44.0),
        create_mesh(22.0, 24.0, 42.0, 48.0, -35.0, 14.0),
        create_mesh(22.0, 24.0, 35.0, 42.0, 1.0, 14.0),
        create_mesh(9.0, 22.0, 47.0, 48.0, -35.0, 14.0),
        create_mesh(9.0, 22.0, 42.0, 47.0, -35.0, -27.0),
        create_mesh(-22.0, 9.0, 47.0, 48.0, -35.0, 14.0),
        create_mesh(-22.0, -21.0, 28.0, 47.0, -35.0, -27.0),
        create_mesh(-21.0, -19.0, 35.0, 47.0, -35.0, -27.0),
        create_mesh(-21.0, -19.0, 28.0, 35.0, -35.0, -30.0),
        create_mesh(-19.0, 9.0, 42.0, 47.0, -35.0, -27.0),
        create_mesh(-22.0, -19.0, 23.0, 28.0, -35.0, -34.0),
        create_mesh(-45.0, -41.0, 26.0, 28.0, -34.0, 18.0),
        create_mesh(-45.0, -41.0, -18.0, 26.0, -34.0, -19.0),
        create_mesh(-41.0, -28.0, 26.0, 28.0, -34.0, 18.0),
        create_mesh(-41.0, -28.0, 23.0, 26.0, -34.0, -19.0),
        create_mesh(-28.0, -21.0, 23.0, 28.0, -34.0, -27.0),
        create_mesh(-21.0, -19.0, 23.0, 28.0, -34.0, -30.0),
        create_mesh(28.0, 32.0, -41.0, -36.0, -35.0, 20.0),
        create_mesh(28.0, 32.0, -36.0, -33.0, -35.0, -8.0),
        create_mesh(28.0, 32.0, -33.0, -30.0, -35.0, -8.0),
        create_mesh(22.0, 28.0, -41.0, -30.0, -35.0, -12.0),
        create_mesh(-15.0, -14.0, -41.0, -29.0, -35.0, -12.0),
        create_mesh(-14.0, 3.0, -41.0, -30.0, -35.0, -12.0),
        create_mesh(3.0, 22.0, -41.0, -30.0, -35.0, -12.0),
        create_mesh(-28.0, -21.0, 26.0, 47.0, -27.0, 28.0),
        create_mesh(-21.0, -19.0, 35.0, 47.0, -27.0, 28.0),
        create_mesh(-21.0, -19.0, 26.0, 35.0, 19.0, 28.0),
        create_mesh(-28.0, -21.0, 23.0, 26.0, -27.0, -19.0),
        create_mesh(-19.0, 3.0, 42.0, 47.0, -27.0, 28.0),
        create_mesh(-19.0, -14.0, 35.0, 42.0, 1.0, 28.0),
        create_mesh(-19.0, -14.0, 26.0, 35.0, 19.0, 28.0),
        create_mesh(-14.0, 3.0, 35.0, 42.0, 1.0, 28.0),
        create_mesh(-14.0, 3.0, 26.0, 35.0, 19.0, 28.0),
        create_mesh(9.0, 22.0, 42.0, 47.0, -27.0, 28.0),
        create_mesh(9.0, 22.0, 35.0, 42.0, 1.0, 28.0),
        create_mesh(9.0, 22.0, 24.0, 35.0, 19.0, 28.0),
        create_mesh(9.0, 22.0, 22.0, 24.0, 19.0, 28.0),
        create_mesh(3.0, 9.0, 42.0, 47.0, -27.0, 28.0),
        create_mesh(3.0, 9.0, 35.0, 42.0, 1.0, 28.0),
        create_mesh(3.0, 9.0, 26.0, 35.0, 19.0, 28.0),
        create_mesh(40.0, 50.0, -29.0, 16.0, -45.0, 5.0),
        create_mesh(28.0, 40.0, -29.0, 16.0, -45.0, -42.0),
        create_mesh(26.0, 28.0, -1.0, 16.0, -45.0, -42.0),
        create_mesh(26.0, 28.0, -29.0, -1.0, -45.0, -42.0),
        create_mesh(9.0, 26.0, -29.0, -5.0, -45.0, -42.0),
        create_mesh(-41.0, -37.0, -29.0, -20.0, -48.0, -1.0),
        create_mesh(-41.0, -37.0, -20.0, 23.0, -48.0, -19.0),
        create_mesh(-27.0, -22.0, -29.0, -20.0, -48.0, -1.0),
        create_mesh(-27.0, -22.0, -20.0, 23.0, -48.0, -19.0),
        create_mesh(-37.0, -27.0, -29.0, -20.0, -48.0, -1.0),
        create_mesh(-37.0, -27.0, -20.0, -17.0, -48.0, -19.0),
        create_mesh(-37.0, -27.0, 1.0, 23.0, -48.0, -19.0),
        create_mesh(-37.0, -27.0, -17.0, 1.0, -48.0, -19.0),
        create_mesh(-22.0, -21.0, -1.0, 23.0, -48.0, -19.0),
        create_mesh(-21.0, -19.0, -1.0, 23.0, -48.0, -30.0),
        create_mesh(-22.0, -19.0, -29.0, -20.0, -48.0, -12.0),
        create_mesh(-22.0, -21.0, -20.0, -1.0, -48.0, -19.0),
        create_mesh(-21.0, -19.0, -20.0, -1.0, -48.0, -30.0),
        create_mesh(-19.0, -14.0, -29.0, -20.0, -48.0, -12.0),
        create_mesh(-19.0, -14.0, -20.0, -5.0, -48.0, -30.0),
        create_mesh(-14.0, 9.0, -29.0, -5.0, -48.0, -42.0),
        create_mesh(-22.0, -19.0, -46.0, -20.0, -12.0, 38.0),
        create_mesh(-22.0, -19.0, -20.0, -1.0, 32.0, 38.0),
        create_mesh(26.0, 28.0, -46.0, -36.0, -12.0, 38.0),
        create_mesh(26.0, 28.0, -36.0, -33.0, -12.0, -8.0),
        create_mesh(26.0, 28.0, -36.0, -33.0, 37.0, 38.0),
        create_mesh(26.0, 28.0, -33.0, -30.0, -12.0, -8.0),
        create_mesh(-19.0, -14.0, -46.0, -20.0, -12.0, 38.0),
        create_mesh(-19.0, -14.0, -20.0, -5.0, 32.0, 38.0),
        create_mesh(-14.0, -10.0, -46.0, -33.0, -12.0, 38.0),
        create_mesh(-10.0, 26.0, -46.0, -36.0, -12.0, 38.0),
        create_mesh(-10.0, 26.0, -36.0, -33.0, -12.0, -8.0),
        create_mesh(-10.0, 26.0, -36.0, -33.0, 37.0, 38.0),
        create_mesh(-14.0, -10.0, -33.0, -30.0, -12.0, -4.0),
        create_mesh(-10.0, 26.0, -33.0, -30.0, -12.0, -8.0),
        create_mesh(-19.0, -14.0, -5.0, -1.0, 32.0, 38.0),
        create_mesh(-19.0, -14.0, 35.0, 42.0, -49.0, 1.0),
        create_mesh(-19.0, -14.0, 26.0, 35.0, -49.0, -30.0),
        create_mesh(-19.0, -14.0, -5.0, 26.0, -49.0, -30.0),
        create_mesh(9.0, 26.0, 35.0, 42.0, -49.0, 1.0),
        create_mesh(9.0, 26.0, 24.0, 35.0, -49.0, -30.0),
        create_mesh(-14.0, 9.0, 35.0, 42.0, -49.0, 1.0),
        create_mesh(-14.0, 9.0, 26.0, 35.0, -49.0, -30.0),
        create_mesh(-14.0, 9.0, 24.0, 26.0, -49.0, -30.0),
        create_mesh(-14.0, 26.0, -5.0, 24.0, -49.0, -42.0),
        create_mesh(37.0, 40.0, -30.0, 24.0, -42.0, 10.0),
        create_mesh(34.0, 37.0, 10.0, 24.0, -42.0, 10.0),
        create_mesh(34.0, 37.0, -30.0, 10.0, -42.0, -8.0),
        create_mesh(27.0, 34.0, 22.0, 24.0, -42.0, 10.0),
        create_mesh(9.0, 27.0, 22.0, 24.0, -42.0, -30.0),
        create_mesh(-14.0, 9.0, 22.0, 24.0, -42.0, -30.0),
        create_mesh(27.0, 34.0, 10.0, 22.0, -42.0, -4.0),
        create_mesh(9.0, 27.0, 10.0, 22.0, -42.0, -30.0),
        create_mesh(27.0, 34.0, -30.0, 10.0, -42.0, -8.0),
        create_mesh(9.0, 27.0, -30.0, -20.0, -42.0, -8.0),
        create_mesh(9.0, 27.0, -20.0, 10.0, -42.0, -30.0),
        create_mesh(-14.0, -10.0, -30.0, -20.0, -42.0, -4.0),
        create_mesh(-10.0, 9.0, -30.0, -20.0, -42.0, -8.0),
        create_mesh(-14.0, 9.0, -20.0, 22.0, -42.0, -30.0),
        create_mesh(27.0, 34.0, 10.0, 22.0, -4.0, 41.0),
        create_mesh(9.0, 27.0, 10.0, 22.0, 19.0, 41.0),
        create_mesh(9.0, 34.0, -33.0, 10.0, 37.0, 41.0),
        create_mesh(-14.0, -10.0, -33.0, -20.0, -4.0, 41.0),
        create_mesh(-10.0, 9.0, -33.0, -20.0, 37.0, 41.0),
        create_mesh(-14.0, -10.0, -20.0, 22.0, 32.0, 41.0),
        create_mesh(-10.0, 9.0, 10.0, 22.0, 32.0, 41.0),
        create_mesh(-10.0, 9.0, -20.0, 10.0, 37.0, 41.0),
        create_mesh(-46.0, -27.0, -20.0, 26.0, -19.0, 32.0),
        create_mesh(-9.0, 9.0, 10.0, 26.0, 19.0, 32.0),
        create_mesh(-27.0, -21.0, -20.0, 7.0, -19.0, 32.0),
        create_mesh(-21.0, -10.0, -20.0, 7.0, 19.0, 32.0),
        create_mesh(-27.0, -21.0, 23.0, 26.0, -19.0, 32.0),
        create_mesh(-21.0, -9.0, 23.0, 26.0, 19.0, 32.0),
        create_mesh(-27.0, -21.0, 7.0, 23.0, -19.0, -8.0),
        create_mesh(-27.0, -21.0, 7.0, 23.0, 10.0, 32.0),
        create_mesh(-21.0, -10.0, 7.0, 23.0, 19.0, 32.0),
        create_mesh(-10.0, -9.0, 10.0, 23.0, 19.0, 32.0),
        create_mesh(-10.0, 6.0, -36.0, -20.0, -8.0, 37.0),
        create_mesh(-10.0, 6.0, -20.0, 10.0, 19.0, 37.0),
        create_mesh(27.0, 37.0, -36.0, 10.0, -8.0, 37.0),
        create_mesh(20.0, 27.0, -36.0, -20.0, -8.0, 37.0),
        create_mesh(20.0, 27.0, -20.0, 10.0, 19.0, 37.0),
        create_mesh(6.0, 20.0, -36.0, -22.0, -8.0, 37.0),
        create_mesh(6.0, 20.0, -12.0, 10.0, 19.0, 37.0),
        create_mesh(6.0, 20.0, -22.0, -20.0, -8.0, -1.0),
        create_mesh(6.0, 20.0, -22.0, -20.0, 18.0, 37.0),
        create_mesh(6.0, 20.0, -20.0, -12.0, 19.0, 37.0),
        create_mesh(-21.0, 27.0, -20.0, 35.0, -30.0, 19.0),
    ];

    loop {
        let delta = get_frame_time();
        let mut boost = false;

        if is_key_pressed(KeyCode::Escape) {
            grabbed = !grabbed;
            set_cursor_grab(grabbed);
            show_mouse(!grabbed);
        }
        if is_key_down(KeyCode::LeftShift) {
            boost = true;
        }

        if is_key_down(KeyCode::W) {
            position += front * (MOVE_SPEED * (if boost {10.0} else {1.0}));
        }
        if is_key_down(KeyCode::S) {
            position -= front * (MOVE_SPEED * (if boost {10.0} else {1.0}));
        }
        if is_key_down(KeyCode::A) {
            position -= right * (MOVE_SPEED * (if boost {10.0} else {1.0}));
        }
        if is_key_down(KeyCode::D) {
            position += right * (MOVE_SPEED * (if boost {10.0} else {1.0}));
        }

        let mouse_position: Vec2 = mouse_position().into();
        let mouse_delta = mouse_position - last_mouse_position;
        last_mouse_position = mouse_position;

        yaw += mouse_delta.x * delta * LOOK_SPEED;
        pitch += mouse_delta.y * delta * -LOOK_SPEED;

        pitch = if pitch > 1.5 { 1.5 } else { pitch };
        pitch = if pitch < -1.5 { -1.5 } else { pitch };

        front = vec3(
            yaw.cos() * pitch.cos(),
            pitch.sin(),
            yaw.sin() * pitch.cos(),
        )
        .normalize();

        right = front.cross(world_up).normalize();
        up = right.cross(front).normalize();

        clear_background(background);

        set_camera(&Camera3D {
            position: position,
            up: up,
            target: position + front,
            ..Default::default()
        });

        for mesh in &meshes {
            draw_mesh(mesh);
        }
    
        // Back to screen space, render some text
        set_default_camera();

        draw_text(
            format!("Use <W,A,S,D> to move, <Shift> to boost").as_str(),
            10.0,
            30.0,
            30.0,
            LIGHTGRAY,
        );
        draw_text(
            format!("X: {:.0} Y: {:.0} Z: {:.0}", position.x, position.y, position.z).as_str(),
            10.0,
            30.0 + 24.0,
            30.0,
            GRAY,
        );
        draw_text(
            format!("yaw: {:.2} pitch: {:.2}", yaw, pitch).as_str(),
            10.0,
            30.0 + 48.0,
            30.0,
            GRAY,
        );

        next_frame().await
    }
}
