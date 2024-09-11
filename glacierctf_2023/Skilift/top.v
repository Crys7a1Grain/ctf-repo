module top(
    input [63:0] key,
    output lock
);
  
    reg [63:0] tmp1, tmp2, tmp3, tmp4;

    // Stage 1
    always @(*) begin
        tmp1 = key & 64'hF0F0F0F0F0F0F0F0;
    end
    
    // Stage 2
    always @(*) begin
        tmp2 = tmp1 <<< 5;
    end
    
    // Stage 3
    always @(*) begin
        tmp3 = tmp2 ^ "HACKERS!";
    end

    // Stage 4
    always @(*) begin
        tmp4 = tmp3 - 12345678;
    end

    // I have the feeling "lock" should be 1'b1
    assign lock = tmp4 == 64'h5443474D489DFDD3;

endmodule



//https://www.jdoodle.com/execute-verilog-online

// module top(
//     output reg lock
// );
  
//     reg [63:0] tmp1, tmp2, tmp3, tmp4;
//     reg [63:0] key = 64'h1234567812345678;

//     always @* begin
//         tmp1 = key; // + 12345678
//     end
    
//     always @* begin
//         tmp2 = tmp1 ^ 64'h4841434B45525321; // Шестнадцатеричное представление строки "HACKERS!"
//     end
    
//     always @* begin
//         tmp3 = tmp2 >>> 5;
//     end

//     always @* begin
//         tmp4 = tmp3 | (64'hFFFFFFFFFFFFFFFF ^ 64'hF0F0F0F0F0F0F0F0);
//     end
    
//     initial begin
//         $display("Value of lock: %h", tmp4);
//         $finish;
//     end

// endmodule